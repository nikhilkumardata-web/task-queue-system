from fastapi import FastAPI
from queue_system import task_queue

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task Queue System Running"}

@app.post("/task")
def add_task(x: int, y: int):
    task_id = task_queue.add_task(x, y)
    return {"task_id": task_id}
