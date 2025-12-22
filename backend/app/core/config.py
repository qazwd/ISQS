from pydantic_settings import BaseSettings
from typing import Optional, List
from secrets import token_urlsafe


class Settings(BaseSettings):
    # 应用基本配置
    APP_NAME: str = "ISQS Backend"
    APP_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True  # 添加DEBUG配置
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./isqs.db"  # SQLite 默认配置
    
    # 安全配置
    SECRET_KEY: str = token_urlsafe(32)  # 自动生成安全密钥
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS配置
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]  # 添加CORS配置
    
    # 日志配置
    LOG_LEVEL: str = "DEBUG"  # 添加日志配置
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        env_parse_env_vars = True

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str):
            if field_name == "ALLOWED_ORIGINS":
                return [origin.strip() for origin in raw_val.split(",")]
            return raw_val


settings = Settings()
