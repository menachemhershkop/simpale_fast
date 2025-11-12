from fastapi import FastAPI, HTTPException
import uvicorn
import json
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    price: float
app= FastAPI()
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data,file)
@app.get("/")
def main_page():
    return {"message":"hello"}

@app.get("/items/")
def item_list():
    return load_data()
@app.put("/items/{item_id}")
def update_data(item :Item):
    items=load_data()
    for i in items:
        if i['id'] == item.id:
            i['price']=item.price
        save_data(i)
        return "Price update",items
    raise HTTPException(status_code=404,detail="Not found")

# if __name__=='__main__':
