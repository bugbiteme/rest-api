from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/hello")
def hello():
    return {"message": "hello world"}

@app.get("/api/v1/hello2")
def hello2():
    return {"message": "hello world2"}
