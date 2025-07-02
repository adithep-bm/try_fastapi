from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None): #q is query string 
    return {"item_id": item_id, "q": q}

@app.post("/items")
# async def create_item(request: Request):
#     item = await request.json()   
#     print(item["name"])            
#     return {"request body": item }
def create_item(item: Item):  #เชื่อม Pydantic model เข้ากับ การรับผ่าน post มา ซึ่งมันทำ automatic ไว้ว่าให้ mapping ตัวที่เป็น field และรับ request ผ่านตัวแปรที่เรียกใช้ได้เลย
    print(item.name)    
    return {"request body": item }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return { "id": item_id,"request body": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}