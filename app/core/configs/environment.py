from pydantic import BaseSettings, Field


class Environment(BaseSettings):

    class Config:
        """Load config file"""

        env_file = ".env"

    APPLICATION_HOST: str = Field(default=None)
    APPLICATION_PORT: int = Field(default=None)
    APPLICATION_NAME: str = Field(default="PaintingRoom")
    DATABASE_HOST: str = Field(default=None)
    DATABASE_NAME: str = Field(default=None)
    DATABASE_USER: str = Field(default=None)
    DATABASE_PASSWORD: str = Field(default=None)
