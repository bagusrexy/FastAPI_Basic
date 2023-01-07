from fastapi import APIRouter
from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db


router = APIRouter()



@router.get("/test")

@router.get("/created{date}")
async def get_created_date(db: Session = Depends(get_db)):
    user = db.query(models.Post).filter(models.Post.created_at == ).first()
    return print("hello world")


@router.get("", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # print(posts)

    return posts