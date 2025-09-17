from fastapi import FastAPI
import uvicorn
from routes import get,post

app = FastAPI()   


@app.get('/')
def root():
    return {"msg":"Ok"}

app.include_router(get.route)




app.include_router(post.route)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port=8000,reload=True)
