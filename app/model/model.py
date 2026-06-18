from sqlalchemy import Column, String, Integer
from app.database.database import Base

class Todo(Base):
    __tablename__="todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)

