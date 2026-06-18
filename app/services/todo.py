from sqlalchemy.orm import Session
from app.model.model import Todo
from app.schemas.todo import TodoCreate


def Create_Todo(db: Session, todo: TodoCreate):

    new_todo = Todo(
        title=todo.title,
        description=todo.description
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

def get_Todos(db: Session):

    all_todo = db.query(Todo).all()

    return all_todo

def get_By_Id(db:Session, id: int):

    toda_data = db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not toda_data:
        return None

    return toda_data


def Update_Data(de:Session, id:int, todo_data: TodoCreate):

    Update_data=db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not Update_data:
        return None

    Update_data.title = toda_data.title
    Update_Data.desctiption = toda_data.description

    db.commit()
    db.refresh(Update_data)

    return Update_data

def Delete_Todo(db: Session, id:int):

    delete_data=db.query(Todo).filter(
        Todo.id == id
    ).first()

    if not delete_data:
        return None

    db.delete(delete_data)
    db.commit()

    return delete_data



