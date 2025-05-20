from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str
    completed: bool

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
