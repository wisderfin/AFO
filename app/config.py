from settings import settings as env


class Config:
    SQLALCHEMY_DATABASE_URI = (f'postgresql+psycopg2://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:'
                               f'{env.DB_PORT}/{env.DB_NAME}')
