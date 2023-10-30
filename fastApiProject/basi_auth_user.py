from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

users_db = {
    "mouredev":{
        'username':'pabloacalvo',
        'full_name': 'pablo calvo',
        'email': 'pablo@live.com',
        'disable': False,
        'password':'123456'
    }
}