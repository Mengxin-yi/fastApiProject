from fastapi import FastAPI, Cookie, Response
from typing import Union
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


@app.get("/books")
async def books(
        ads_id: Annotated[Union[str, None], Cookie()]
):
    return {
        "code": 200,
        "message": "访问成功",
        "ads_id": ads_id
    }

