from fastapi import FastAPI
from agent import run_pipeline
import threading
import time

app = FastAPI()

# =========================
# MANUAL TRIGGER (DEBUG)
# =========================
@app.post("/run")
def trigger():
    run_pipeline()
    return {"status": "executed"}

# =========================
# AUTONOMOUS WORKER LOOP
# =========================
def background_worker():
    while True:
        try:
            print("AUTO-RUN: executing pipeline...")
            run_pipeline()
        except Exception as e:
            print("WORKER ERROR:", e)

        time.sleep(300)  # every 5 minutes

# start worker thread on boot
threading.Thread(target=background_worker, daemon=True).start()

# health check
@app.get("/")
def home():
    return {"status": "AUTONOMOUS AI SALES AGENT RUNNING"}
