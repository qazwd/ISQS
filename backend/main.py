import uvicorn
from app.core.config import settings
from app import app


if __name__ == "__main__":
    # 启动FastAPI应用
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True  # 在开发环境中启用自动重载
    )
