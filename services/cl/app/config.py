from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_name: str = "bank-cl"
    jwt_secret: str = "wecode-bank-demo-secret-change-me"
    max_contacts_per_day: int = 3

settings = Settings()
