from fastapi import FastAPI
from pydantic import BaseModel
from env import MiniEnv

app = FastAPI()
env = MiniEnv()

class ActionInput(BaseModel):
    action: int

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(data: ActionInput):
    return env.step(data.action)