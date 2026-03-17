from fastapi import FastAPI
from tasks import add_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task Queue System Running"}

@app.post("/task")
def create_task(x: int, y: int):
    result = add_task(x, y)
    return {"result": result}
