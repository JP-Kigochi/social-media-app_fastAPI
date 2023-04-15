from typing import List, Optional
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2, database
from sqlalchemy.orm import Session
from sqlalchemy import func


#creating the posts router
router = APIRouter(
        prefix = "/posts",
        tags = ['Posts']
)

#Creating a route for getting posts
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    posts= db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
    
#Creating a route for creating a new post
@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):    
    new_post = models.Post(user_id= current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

#Creating a route for getting a post from a specific user
@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)): 
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id,{id}, was not Found")
    return post

#Creating a route for deleting a post
@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id )
    post= post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Creating a route for updating a post
@router.put("/{id}", status_code= status.HTTP_201_CREATED, response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id )
    post = post_query.first()
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()