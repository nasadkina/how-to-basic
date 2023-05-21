import uvicorn
from fastapi import FastAPI

app = FastAPI()


# @app.get
# def app('/')
#     return {"message": hui}
@app.get('/ping/')
def root():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
