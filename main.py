from item import Item
from fastapi import FastAPI

app = FastAPI()

data_store = {
    1: Item(name="Foo", price=50.2),
    2: Item(name="Bar", price=62, description="The bartenders"),
    3: Item(name="Baz", price=50.2, description="Not the bartenders"),
}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # read from in-memory data store
    return data_store[item_id]

@app.post("/items/")
def create_item(item: Item):
    # add to in-memory data store
    # add!
    # insert

    item_id = max(data_store.keys()) + 1
    data_store[item_id] = item

    return item # 👍

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # delete from in-memory data store
    del data_store[item_id]
    return {"message": "Item deleted successfully!"}

@app.get("/items/")
def read_items():
    # read a list of item price, name, and description combined with the id from the in-memory data store
    return [{"id": k, **v.dict()} for k, v in data_store.items()]