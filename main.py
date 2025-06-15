# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "مرحباً بك في API Elrouby!"}

@app.get("/postapi")
def postapi():
    return "Number"