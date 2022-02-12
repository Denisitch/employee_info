from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://db_user:db_pass@db/db_name"


settings = Settings()
