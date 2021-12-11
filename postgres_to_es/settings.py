from pydantic import BaseSettings


class ETLSettings(BaseSettings):
    postgres_db: str = 'cinema'
    postgres_host: str = 'db'
    postgres_port: int = 5432
    postgres_user: str = 'cinema'
    postgres_password: str = 'cinema'
    postgres_schema: str = 'public,content'
    redis_prefix: str = ''
    redis_host: str = 'redis'
    redis_port: int = 6379
    redis_password: str = ''
    elastic_host: str = 'elastic'
    elastic_port: int = 9200
    elastic_scheme: str = 'http'
    elastic_user: str = 'elastic'
    elastic_password: str = ''
    elastic_index: str = 'movies'
    etl_size_limit: int = 10

    class Config:
        env_file = '../.env'
