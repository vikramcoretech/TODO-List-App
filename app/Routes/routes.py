from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.todo import TodoCreate
from app.services.todo import *

router = APIRouter(
    prefix="/todos",
    tags=["Test"]
)


@router.post("/")
def create(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return Create_Todo(db, todo)


@router.get("/")
def get_all(
    db: Session = Depends(get_db)
):
    return get_Todos(db)


@router.get("/{todo_id}")
def get_one(
    todo_id: int,
    db: Session = Depends(get_db)
):
    return get_By_Id(db, todo_id)


@router.put("/{todo_id}")
def update(
    todo_id: int,
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    return Update_Data(
        db,
        todo_id,
        todo
    )


@router.delete("/{todo_id}")
def delete(
    todo_id: int,
    db: Session = Depends(get_db)
):
    return Delete_Todo(
        db,
        todo_id
    )