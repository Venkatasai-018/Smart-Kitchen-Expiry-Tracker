from fastapi import FastAPI
import uvicorn
from routes import get,post,delete

app = FastAPI()   


@app.get('/')
def root():
    return {"msg":"Ok"}

app.include_router(get.route)




app.include_router(post.route)
app.include_router(delete.route)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000,reload=True)
