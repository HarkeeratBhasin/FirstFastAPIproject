from typing import Union

from fastapi import FastAPI

from fastapi.responses import PlainTextResponse

from fastapi.responses import HTMLResponse

from typing import Optional

from pydantic import BaseModel

app = FastAPI()

# Fast API reads and executes the code from top to bottom line by line

@app.get("/")
async def ogpage():
    return PlainTextResponse("Hello World")

@app.get("/blog")
async def index(limit=10,published:bool = True, sort:Optional[str] = None):
    if published:   
        return PlainTextResponse(f'{limit} published blogs from the database')
    else:
        return PlainTextResponse(f'{limit} unpublished blogs from the database')

@app.get("/blog/unpublished")
async def unpublished():
    return PlainTextResponse("all unpublished blogs")

@app.get("/blog/{id}")
async def show(id:int):
    #fetch blog with id = id
    return PlainTextResponse(f'blog with id {id}')

@app.get("/blog/{id}/comments")
async def comments(id,limit=10):
    #fetch comments of blog with id = id
    return PlainTextResponse(f'blog comments with id {id} and limit {limit}')

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
@app.post("/blog")
async def create_blog(blog:Blog):
    return PlainTextResponse(f'blog created with title {blog.title}')
