from pydantic import BaseModel

class TodoCreate(BaseModel):
    title:str
    description:str

class TodoResponse(TodoCreate):
    id:int

    class config():
        form_attributes=True