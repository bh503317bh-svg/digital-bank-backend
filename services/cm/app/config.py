from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_name: str = "bank-cm"
    jwt_secret: str = "wecode-bank-demo-secret-change-me"
    sla_hours_p1: int = 4
    sla_hours_p2: int = 24
    sla_hours_p3: int = 72

settings = Settings()
