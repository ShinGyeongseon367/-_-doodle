from asyncio.log import logger
from tkinter.messagebox import NO
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get("/")
def read_root():
    return {"Hello":"Wrold"}

@app.get("/items/{item_id}")
# def read_item(item_id : int , q: Optional[str] = None):
def read_item(item_id : int):
    # return {"item_id" : item_id , "q" : q}
    return {"item_id" : item_id}

@app.put("/items/{item_id}")
def update_item(item_id : int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print("model_name_value ::: ", model_name.value, " typeof ::: ", type(model_name.value))
    print("model_name_alexnet ::: ", model_name.alexnet, "typeof ::: ", model_name.alexnet)

    return {"model_name" : model_name}

@app.get("/models/{model_number}/temp") #순서로 가능하긴하지만 , 
async def get_model_02(model_number: int):
    print("model_number ::: ", model_number)
    return {'return_model_number' : model_number}


########################################################이런식으로 http method get을 선언해주는 과정에서 순서도 굉장히 중요한 요소가 될 수 있다. 
@app.get("/users/me")
async def get_users():
    return {"user_name": "None"}

@app.get("/users/{user_id}")
async def get_users(user_id: int):
    return {"user_id": user_id}

