# main.py
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Sample OpenAPI-compatible API",
    version="1.0.0",
    description="A simple stub server compatible with OpenAPI.",
)


# リクエストボディ用モデル
class CreateItemRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# レスポンス用モデル
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# シンプルなヘルスチェック
@app.get("/health", summary="Health check", tags=["system"])
def health_check():
    return {"status": "ok"}


# IDでアイテム取得 (スタブ)
@app.get(
    "/items/{item_id}",
    response_model=Item,
    summary="Get an item by ID",
    tags=["items"],
)
def get_item(item_id: int):
    # 本来はDBなどから取得するが、スタブなので固定値を返す
    return Item(
        id=item_id,
        name=f"Item {item_id}",
        description="This is a stub item.",
        price=100.0,
    )


# アイテム作成 (スタブ)
@app.post(
    "/items",
    response_model=Item,
    summary="Create a new item",
    tags=["items"],
)
def create_item(body: CreateItemRequest):
    # 本来はDBに保存してIDを発行するが、スタブなので固定ID
    return Item(
        id=1,
        name=body.name,
        description=body.description,
        price=body.price,
    )
