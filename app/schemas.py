from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
