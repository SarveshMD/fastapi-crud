from fastapi import FastAPI, HTTPException, Response, status, Depends
import uuid
from sqlalchemy import select
from sqlalchemy.orm import Session

# from toy_data import toy_data
from schemas import TaskCreate, TaskResponse, TaskUpdate
from models import Task
from database import get_db, Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

# tasks = toy_data['Tasks']

@app.get("/")
def home():
    return {"message": "a never ending midnight sun!"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.scalars(select(Task)).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@app.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def put_task(task_id: uuid.UUID, new_task: TaskCreate, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    task.title = new_task.title
    task.description = new_task.description
    task.priority = new_task.priority
    task.is_completed = False

    db.commit()
    db.refresh(task)
    return task

@app.patch("/tasks/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: uuid.UUID, task_data: TaskUpdate, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    updates = task_data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    db.delete(task)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


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