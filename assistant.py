"""Authenticated DeepSeek assistant. The provider key never reaches the browser."""
import json
import os
import math
import logging
import re
from typing import Literal

import httpx
from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, Field
from bank_common import decode_token

router = APIRouter()
logger = logging.getLogger(__name__)
PAGES = {
    "account": ("/", "Account overview", "View accounts and balances", "balance-o"),
    "mine": ("/mine", "Account center", "Profile, accounts and services", "user-o"),
    "wealth": ("/wealth", "Explore wealth", "Browse investment products", "chart-trending-o"),
    "funds": ("/funds", "Explore funds", "Browse funds and ETFs", "chart-trending-o"),
    "transfer": ("/transfer", "Make a transfer", "Explore transfer options", "exchange"),
    "transfer_in": ("/transfer-in", "Add money", "See ways to add funds", "plus"),
    "transactions": ("/transactions", "Transaction history", "Review account activity", "orders-o"),
    "orders": ("/orders", "Transfer status", "Review transfer orders", "orders-o"),
    "cards": ("/cards", "Bank cards", "View and manage cards", "card-o"),
    "loans": ("/loans", "Loans", "Explore loan options", "balance-o"),
    "security": ("/security", "Security center", "Manage security settings", "shield-o"),
    "holdings": ("/holdings", "Investment holdings", "Review your holdings", "chart-trending-o"),
    "fx": ("/fx", "Currency exchange", "Explore exchange options", "exchange"),
    "bills": ("/bills", "Bills & disputes", "View bills and disputes", "orders-o"),
    "payees": ("/payees", "Payees", "Manage recipients", "friends-o"),
    "schedule": ("/schedule", "Scheduled transfers", "Review scheduled transfers", "clock-o"),
    "kyc": ("/kyc", "Identity verification", "Check verification details", "contact-o"),
    "pay": ("/pay", "Payments", "Explore payment options", "balance-pay"),
    "points": ("/points", "Rewards", "Explore points and rewards", "gift-o"),
    "notices": ("/notices", "Notifications", "Review account notices", "bell"),
    "rights": ("/rights", "Benefits", "Explore member benefits", "gift-o"),
}
PRODUCTS = {"f1": "IBB", "f2": "QQQ", "f3": "VIG", "f4": "SPY", "f5": "XLK", "f6": "XLV", "f7": "GLD", "f8": "TLT", "f9": "ARKK", "f10": "VTI", "f11": "ASEA", "f12": "EWS", "f13": "EWM", "f14": "EIDO", "f15": "THD", "f16": "VNM", "f17": "EPHE"}

# These keywords are a fallback when the provider cannot return structured actions.
GUIDE_PATTERNS = (
    ("orders", r"\border\b|\borders\b|transfer status|track (?:a |my |the )?(?:transfer|payment)"),
    ("transactions", r"transaction|statement|account activity|payment history"),
    ("holdings", r"holdings?|portfolio|my investments?"),
    ("account", r"account|balance|balances"),
    ("transfer_in", r"add (?:money|funds)|fund (?:my |the )?account|deposit money"),
    ("schedule", r"schedul(?:e|ed|ing).*transfer|recurring transfer"),
    ("transfer", r"\btransfers?\b|send (?:money|funds)|\bwire\b"),
    ("payees", r"payee|beneficiar|recipient"),
    ("cards", r"\bcards?\b|debit|credit card"),
    ("loans", r"\bloans?\b|borrow|repay"),
    ("security", r"security|password|fraud|lock (?:my )?account"),
    ("fx", r"exchange rate|currency exchange|convert currency|foreign exchange|\bforex\b"),
    ("bills", r"\bbills?\b|dispute"),
    ("kyc", r"\bkyc\b|verify (?:my |your )?identity|identity verification"),
    ("points", r"\bpoints\b|rewards?"),
    ("rights", r"benefits?|perks?"),
    ("notices", r"notification|alert"),
    ("funds", r"\bfunds?\b|\betfs?\b|invest(?:ment|ing)?|product|\bstocks?\b"),
    ("wealth", r"wealth|savings? products?"),
)


def resolve_actions(suggestions, user_text, reply):
    """Resolve only known app destinations, with context-aware fallback suggestions."""
    actions = []
    seen = set()
    def add(kind, item_id, amount=None):
        if not isinstance(kind, str) or not isinstance(item_id, str) or (kind, item_id) in seen or len(actions) >= 4:
            return
        if kind == "page" and item_id in PAGES:
            path, label, description, icon = PAGES[item_id]
            action = {"path": path, "label": label, "description": description, "icon": icon}
        elif kind == "product" and item_id in PRODUCTS:
            ticker = PRODUCTS[item_id]
            query = {"id": item_id}
            # A model-proposed amount is accepted only if the user explicitly typed it.
            if (isinstance(amount, (int, float)) and not isinstance(amount, bool)
                    and math.isfinite(amount) and 0 < amount <= 10000000
                    and re.search(r"(?<![\d.])" + re.escape(str(amount)) + r"(?![\d.])", user_text)):
                query["amount"] = str(amount)
            action = {"path": "/wealth/detail", "query": query, "label": f"Explore {ticker}",
                      "description": "View product details and risks", "icon": "chart-trending-o"}
        else:
            return
        seen.add((kind, item_id))
        actions.append(action)

    # Explicit product requests take priority over more general suggestions.
    for product_id, ticker in PRODUCTS.items():
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(ticker) + r"(?![A-Za-z0-9])", user_text, re.I):
            matching = next((item for item in suggestions if isinstance(item, dict) and item.get("kind") == "product" and item.get("id") == product_id), {}) if isinstance(suggestions, list) else {}
            add("product", product_id, matching.get("amount"))

    if isinstance(suggestions, list):
        for suggestion in suggestions[:12]:
            if isinstance(suggestion, dict):
                kind, item_id = suggestion.get("kind"), suggestion.get("id")
                if kind == "product":
                    ticker = PRODUCTS.get(item_id) if isinstance(item_id, str) else None
                    if not ticker or not re.search(r"(?<![A-Za-z0-9])" + re.escape(ticker) + r"(?![A-Za-z0-9])", user_text + " " + reply, re.I):
                        continue
                add(kind, item_id, suggestion.get("amount"))

    # Only surface products from the reply when the user is asking about investments.
    product_question = re.search(r"product|fund|\betf|invest|\bstock|\bqqq\b|\bspy\b|\bgld\b|\bvti\b", user_text, re.I)
    if product_question:
        for product_id, ticker in PRODUCTS.items():
            if re.search(r"(?<![A-Za-z0-9])" + re.escape(ticker) + r"(?![A-Za-z0-9])", reply, re.I):
                add("product", product_id)
                if len(actions) >= 3:
                    break

    for page_id, pattern in GUIDE_PATTERNS:
        if re.search(pattern, user_text, re.I):
            add("page", page_id)
    return actions


def guide_context(messages):
    current = messages[-1].content
    # Follow-up pronouns can refer to the preceding user request.
    if len(messages) > 1 and len(current) < 100 and re.search(r"\b(it|them|these|those|that|their|its|this|one)\b", current, re.I):
        previous = next((message.content for message in reversed(messages[:-1]) if message.role == "user"), "")
        return current + " " + previous
    return current

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=4000)

class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(min_length=1, max_length=24)

BASE_SYSTEM = """You are aku-bank's helpful banking demo assistant. Respond only in English, accurately and concisely. You are a conversational AI, not a person. You can answer general banking and investment questions, explain how to use this app, and suggest navigating to its pages. Do not claim to have accessed account balances, holdings, prices, live market data, or to have placed transactions: you have not. Never ask for passwords, card numbers, API keys, or other secrets. Do not promise returns or present historical returns as guaranteed. For investments explain relevant risks and avoid pretending to know the user's risk profile. If asked to execute a transaction, explain the user must review and confirm it in the app. You cannot execute it. The app's transfer status page shows transfer orders, not all investment orders; the cards page shows demo debit and linked cards, not a comprehensive credit-card account. Distinguish these capabilities when directing customers. The app's demo fund catalogue contains QQQ (Nasdaq 100), SPY (S&P 500), VTI (US total market), GLD (gold), TLT (long-term US Treasuries), and IBB (biotech). This list is illustrative, not personalized advice; ask about the user's goals and risk tolerance before recommending. Do not invent current prices or returns. The user must review all information before any purchase."""
SYSTEM = BASE_SYSTEM + """ Act as a helpful concierge: answer the question and suggest up to four relevant next steps in the app. Return a valid JSON object with exactly these keys: reply (string), actions (array of objects). Each action must be either {"kind":"page","id":"PAGE_ID"} or {"kind":"product","id":"PRODUCT_ID"}. Available page IDs: account (account overview and balances), mine (account center), wealth (wealth products), funds (fund catalogue), transfer (transfer options), transfer_in (add funds), transactions (account transaction history), orders (transfer status, not investment orders), cards, loans, security, holdings, fx, bills, payees, schedule (scheduled transfers), kyc, pay, points, notices, rights. Valid product IDs: f1 IBB, f2 QQQ, f3 VIG, f4 SPY, f5 XLK, f6 XLV, f7 GLD, f8 TLT, f9 ARKK, f10 VTI, f11 ASEA, f12 EWS, f13 EWM, f14 EIDO, f15 THD, f16 VNM, f17 EPHE. Only recommend products mentioned in the answer or request; do not invent products, claim to know suitability, prices, returns, account data or transaction status. If a specific product was requested, include its product action. For product discovery suggest relevant example product actions and the funds or wealth page. For order and account questions offer the matching pages. Do not mention navigation buttons unless you have included corresponding actions. Return actions: [] for unrelated questions. Never execute or claim to have executed transactions. Do not put markdown fences around JSON."""

async def completion(client, payload, key):
    response = await client.post("https://api.deepseek.com/chat/completions", json=payload,
                                 headers={"Authorization": f"Bearer {key}"})
    if response.status_code in (401, 402, 429):
        messages = {401: "DeepSeek API key was rejected.", 402: "DeepSeek account has insufficient balance.", 429: "DeepSeek is busy. Please try again shortly."}
        raise HTTPException(status_code=502, detail=messages[response.status_code])
    response.raise_for_status()
    choice = response.json()["choices"][0]
    if choice.get("finish_reason") != "stop":
        raise ValueError("Incomplete model response")
    content = choice["message"]["content"]
    if not isinstance(content, str) or not content.strip():
        raise ValueError("Empty model response")
    return content.strip()

@router.post("/api/assistant/chat")
async def chat(body: ChatRequest, authorization: str | None = Header(default=None)):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="Please sign in again.")
    try:
        decode_token(authorization.split(" ", 1)[1], secret=os.environ.get("JWT_SECRET", ""))
    except Exception:
        raise HTTPException(status_code=401, detail="Please sign in again.")
    if body.messages[-1].role != "user":
        raise HTTPException(status_code=422, detail="The last message must be from the user.")
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise HTTPException(status_code=503, detail="The assistant is not configured.")
    payload = {
        "model": os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-pro"),
        "messages": [{"role": "system", "content": SYSTEM}] + [m.model_dump() for m in body.messages],
        "response_format": {"type": "json_object"},
        "thinking": {"type": "disabled"},
        "max_tokens": 1600,
    }
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(45, connect=10)) as client:
            try:
                answer = json.loads(await completion(client, payload, key))
                if not isinstance(answer, dict) or not isinstance(answer.get("reply"), str) or not answer["reply"].strip():
                    raise ValueError("Invalid structured reply")
            except (ValueError, KeyError, IndexError, TypeError):
                # DeepSeek can return whitespace or malformed JSON even with JSON mode enabled.
                # Retry as plain text rather than showing an error to the user.
                logger.warning("DeepSeek returned an invalid structured reply; retrying as text")
                fallback = dict(payload)
                fallback.pop("response_format")
                fallback["messages"] = [{"role": "system", "content": BASE_SYSTEM + " Reply in plain text."}] + [m.model_dump() for m in body.messages]
                reply = await completion(client, fallback, key)
                actions = resolve_actions([], guide_context(body.messages), reply)
                return {"reply": reply, "actions": actions, "action": actions[0] if actions else None}
        reply = answer["reply"]
        suggestions = answer.get("actions", [])
        if not isinstance(suggestions, list):
            suggestions = []
        # Accept the previous single-action format during rollout.
        if answer.get("page") == "product":
            suggestions.append({"kind": "product", "id": answer.get("product_id"), "amount": answer.get("amount")})
        elif answer.get("page"):
            suggestions.append({"kind": "page", "id": answer.get("page")})
        actions = resolve_actions(suggestions, guide_context(body.messages), reply)
        return {"reply": reply.strip(), "actions": actions, "action": actions[0] if actions else None}
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="DeepSeek timed out. Please try again.")
    except (httpx.HTTPError, ValueError, KeyError, IndexError, TypeError):
        logger.warning("DeepSeek request failed or produced an invalid response")
        raise HTTPException(status_code=502, detail="The assistant could not respond. Please try again.")
