from settings import settings as env


class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}'
    JWT_SECRET_KEY = env.JWT_KEY
