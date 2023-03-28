from pydantic import BaseSettings, Field


class Environment(BaseSettings):

    class Config:
        """Load config file"""

        env_file = ".env"

    APPLICATION_HOST: str = Field(default=None)
    APPLICATION_PORT: int = Field(default=None)
    APPLICATION_NAME: str = Field(default="ETL-NEWS")

    DATABASE_HOST: str = Field(default=None)
    DATABASE_NAME: str = Field(default=None)
    DATABASE_USER: str = Field(default=None)
    DATABASE_PASSWORD: str = Field(default=None)

    RBMQ_HOST: str = Field(default=None)
    RBMQ_USER: str = Field(default=None)
    RBMQ_PASS: str = Field(default=None)
    RBMQ_PORT: int = Field(default=None)
    RBMQ_EXCHANGE: str = Field(default=None)

    EXTRACT_CHANNEL: str = Field(default=None)
    EXTRACT_POST_CHANNEL: str = Field(default=None)
    EXTRACT_NEWS_CHANNEL: str = Field(default=None)

    RAW_POSTS_URL: str = Field(default=None)
    BATCH_SIZE: int = Field(default=None)
