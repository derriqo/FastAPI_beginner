from fastapi import FastAPI


app = FastAPI()





@app.post('/blog')
def create(request:Blog):
    return request