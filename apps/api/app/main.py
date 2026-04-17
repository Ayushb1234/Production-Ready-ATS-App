from fastapi import FastAPI
from app.core.database import Base, engine
from app.models.user import User
from app.api.routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)



app = FastAPI(title="App is Running")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)


@app.get("/")
def check():
    return {"message": "App is Running"}