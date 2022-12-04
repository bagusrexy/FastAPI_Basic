from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # print(posts)

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def createpost(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTscO posts (title, konten, published) VALUES (%s, %s, %s) RETURNING * """, 
    #                 (post.title, post.konten, post.published))
    # new_post =  cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(
        **post.dict()
    )
    db.add(new_post)
    db.commit() 
    db.refresh(new_post)
    return new_post

@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * from posts WHERE  id = %s """, (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"post id : {id} tidak ditemukan")
    return{"post_detail": post}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(id),))
    # delete_post = cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post dengan id {id} tidak ditemukan")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):

    # cursor.execute("""UPDATE posts SET title = %s, konten = %s, published = %s WHERE id = %s RETURNING *""", 
    #                 (post.title, post.konten, post.published, str(id)))
    # updated_post = cursor.fetchone()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post dengan id {id} tidak ditemukan")
 
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
    
@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * from posts WHERE  id = %s """, (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"post id : {id} tidak ditemukan")
    return{"post_detail": post}

print("hello world")