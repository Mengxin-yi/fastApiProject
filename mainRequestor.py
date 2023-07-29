from fastapi import FastAPI, Query
from enum import Enum
from typing import List, Union
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class ItemNameSex(Enum):  # 性别预设值
    sex1 = "男"
    sex2 = "女"


class ItemNameDetails(BaseModel):
    sex: ItemNameSex
    age: int
    email: str
    url: HttpUrl  # 验证字段是否为http地址


class Item(BaseModel):
    name: str
    nameDetails: Union[ItemNameDetails, None] = None
    description: Union[str, None] = Field(default=None)
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def main():
    return {"code": 200, "message": "mainRequestor主页"}


@app.get('/books/{user_id}')  # 查询参数
async def getbook(user_id: int, book_id: Union[str, None] = None):
    return {"code": 200, "user_id": user_id, "book_id": book_id, "message": "查询成功"}


@app.post("/items/{user_id}")  # 请求体 路由参数 查询参数  Query 参数验证 default=... 为必要参数  pattern=^123$ 为正则表达式
async def create_item(
        item: Item, user_id: int,
        # q 为多个参数时 则要使用List来进行存储 反之 q只会记录最后一个 （http://localhost:8000/items/?q=foo&q=bar） List下为 q = ['foo','bar'] 未使用List q = 'bar'
        q: Union[List[str], None] = Query(default=..., max_length=50, )
):
    return {
        "user_id": user_id,
        "q": q,
        "item": item
    }
