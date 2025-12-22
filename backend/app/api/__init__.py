from fastapi import APIRouter
from app.api.v1 import api_router as v1_router


# 创建API路由实例
api_router = APIRouter()

# 包含v1版本路由
api_router.include_router(v1_router, prefix="/v1", tags=["v1"])
