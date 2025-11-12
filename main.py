from fastapi import FastAPI, HTTPException
import uvicorn
import json

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
@app.put("/itens/{item_id}")
def update_data(item_id, price):
    items=load_data()
    for i in items:
        if i['id'] == item_id:
            i['price']=price
        save_data(i)
    raise HTTPException(status_code=404,detail="Not found")

if __name__=='__main__':
    uvicorn.run(app, host='localhost',port=8000, reload=True)