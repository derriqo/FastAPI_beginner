from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/blog')

def index(limit = 10,published : bool = True, sort : Optional[str] = None):

    #only get 10 published blogs


    if published:

        return {'message': f'{limit} published blog from the db'}
    else:
        return {'message': f'{limit} blog from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):

    #fetch comments of blog with id = id
    return limit
    return {'data':{'1','2'}}

    
class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    
    return {'data':f'Blog is created with title as {request.title}'}