from fastapi import FastAPI
from item import Item

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
    # read from in-memory store
    return data_store[item_id]

@app.put("/items/")
def create_item(item: Item):
    # add to in-memory store
    item_id = max(data_store.keys()) + 1
    data_store[item_id] = item

    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # delete from in-memory store
    del data_store[item_id]
    return {"message": "Item deleted successfully!"}

@app.get("/items/")
def read_items():
    # read from in-memory store, combined with ids
    return [{"id": k, "name": v.name, "price": v.price, "description": v.description} for k, v in data_store.items()]

