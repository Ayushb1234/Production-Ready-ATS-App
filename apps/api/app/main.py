from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="App is Running")

@app.get("/")
def check():
    return {"message": "App is Running"}