from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DataBase_Url = "sqlite:///./todo.db"

engine=create_engine(
    DataBase_Url,
    connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()