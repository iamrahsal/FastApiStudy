from fastapi import FastAPI

app = FastAPI()
#give app as object

#GET as operation
@app.get("/")
def index():
    return {"Hello": "World"}