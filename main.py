from fastapi import FastAPI, HTTPException, status
from typing import List

from repositories import PostRepository
from schemas import Post, PostCreate
from services import PostService

app = FastAPI()

post_repo = PostRepository()
post_service = PostService(post_repo)


@app.get("/")
async def root():
    return {"message": "Hello from main"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"} #기모띠


@app.get("/posts", response_model=List[Post])
async def list_posts():
    return post_service.list_posts()


@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: int):
    post = post_service.get_post(post_id)
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(payload: PostCreate):
    return post_service.create_post(payload)


@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: int, payload: PostCreate):
    updated = post_service.update_post(post_id, payload)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    if post_service.delete_post(post_id):
        return
    raise HTTPException(status_code=404, detail="Post not found")
