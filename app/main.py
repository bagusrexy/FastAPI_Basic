from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='12345', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

        
app.include_router(
    post.router,
    prefix="/posts",
    tags=['posts'])
app.include_router(
    user.router,
    prefix="/users",
    tags=['users'])
app.include_router(
    auth.router,
    tags=['Authenticaton'])

print("hello world")


@app.get("/")
def read_root():
    return {"Hello": "World"}



