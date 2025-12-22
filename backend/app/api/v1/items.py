from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.api.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_items(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """获取所有项目"""
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]

@router.get("/{item_id}", response_model=dict)
def get_item(item_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """获取单个项目"""
    return {"id": item_id, "name": f"Item {item_id}"}
