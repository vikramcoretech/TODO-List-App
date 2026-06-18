from fastapi import FastAPI

from app.database.database import engine
from app.database.database import Base

from app.Routes.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Todo API Running"
    }