from fastapi import FastAPI, HTTPException, status
from toy_data import toy_data
from schemas import TaskCreate, TaskResponse
from uuid import uuid4
from datetime import datetime

app = FastAPI()

tasks = toy_data['Tasks']

@app.get("/")
def home():
    return {"message": "a never ending midnight sun!"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_posts():
    return tasks

@app.get("/task/{task_id}", response_model=TaskResponse)
def get_post(task_id: str):
    for task in tasks:
        if task_id == task.get('id'):
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_id = uuid4()
    new_task = {
        "id": str(new_id),
        "title": task.title,
        "description": task.description,
        "is_completed": False,
        "priority": task.priority,
        "created_at": str(datetime.now())
    }
    tasks.append(new_task)
    return new_task


'''
{
    "id": "6a89a82c197993b55a2322fc",
    "title": "Adipisicing occaecat excepteur incididunt elit.",
    "description": None,
    "is_completed": True,
    "priority": "low",
    "created_at": "Thu Apr 01 1982 15:07:58 GMT+0530 (India Standard Time)"
}
'''