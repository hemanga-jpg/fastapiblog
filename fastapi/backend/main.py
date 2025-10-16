from fastapi import FastAPI
from Core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return{"Hello Charith welcome to FastAPI"}