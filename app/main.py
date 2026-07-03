from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
<<<<<<< HEAD
    return {"item_id": item_id, "q": q}

    
=======
    return {"item_id": item_id, "q": q}
>>>>>>> d53a5f1 (fastapi-structure)
