from fastapi import FastAPI
from enum import Enum
from typing import Union

app = FastAPI()


class ModelsSex(Enum):  # 预设模型
    Sex1 = "男"
    Sex2 = "女"


@app.get("/")
async def main():
    return {"message": "主页"}


@app.get("/items/{item_id}")
async def getitme(item_id: int):
    return {'code': 200, "data": item_id}


#  路径参数
@app.get("/files/{file_path}")
async def getfiles(file_path: str):  # 类型定义
    return {"code": 200, "file_path": file_path}


#  预设值使用
@app.get("/model/{modelSex}")
async def getmodelName(modelSex: ModelsSex):
    if modelSex is ModelsSex.Sex1:
        return {'sex': modelSex}
    return {'sex': modelSex}


@app.get("/books/")
async def getbook(skip: int = 0,
                  limit: int = 10):  # http://127.0.0.1:8000/books/?skip=1&limit=10   # 参数类型赋值等于默认值未传参数时使用
    return {'code': 200, "message": "查询成功", "book": [i for i in range(skip, limit)]}


@app.get('/books2/{user_id}/items/{item_id}')  # 多个参数
async def getbook2(user_id: int, item_id: int, q: Union[str, None] = None, short: bool = False):
    return {'code': 200, "message": "查询成功", "user_id": user_id, "item_id": item_id, "q": q, "short": short,
            "bookName": '龙族'}


