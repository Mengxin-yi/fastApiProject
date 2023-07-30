from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from uuid import UUID

app = FastAPI()

userdata = {
    "易安祺": "1263456",
    "1975941469@qq.com": "520521Yi",
    "1975941469": "520521yi"
}


@app.get("/")
async def homepage():
    return {
        "code": 200,
        "message": "主页"
    }


class PersonalInfo(BaseModel):
    sex: str
    age: int
    email: str


class UserInfo(BaseModel):
    account: str
    password: str
    userPersonalInfo: Union[PersonalInfo,] = None


@app.post("/login")
async def login(userInfo: UserInfo):
    if userdata.get(userInfo.account, ''):
        if userdata.get(userInfo.account, '') == userInfo.password:
            return {
                "code": 200,
                "message": "登录成功"
            }
    return {
        "code": 400,
        "message": "邮箱或用户名与密码不匹配！"
    }


@app.post("/register")
async def register(userInfo: UserInfo):
    print(userInfo)
    if userdata.get(userInfo.account, ""):
        return {
            "code": 200,
            "message": "已注册"
        }
    userdata.update({userInfo.account: userInfo.password})
    return {
        "code": 200,
        "message": "注册成功"
    }


@app.get("/getuuid")
async def getuuid(uuid: UUID):
    return {
        "uuid": uuid
    }
