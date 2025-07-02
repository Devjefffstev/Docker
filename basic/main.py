# install sudo apt install python3-pip
# install pip install fastapi uvicorn | python3 -m pip install fastapi uvicorn
# sudo apt install uvicorn
# to tun the app locally | uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your Dockerized API!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
