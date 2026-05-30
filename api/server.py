from fastapi import FastAPI
from agent import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"status": "agenticmodel running clean"}

@app.post("/run")
def trigger():
    try:
        run_pipeline()
        return {"status": "executed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
