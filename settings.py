from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    BCRYPT_LOG_ROUNDS: int
    SECRET_KEY: str

    class Config:
        env_file = '.env'


settings = Settings()
