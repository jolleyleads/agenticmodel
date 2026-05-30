from fastapi import FastAPI
from agent import run

app = FastAPI()

@app.get('/')
def home():
    return {'status': 'agenticmodel upgraded to SaaS core'}

@app.post('/run')
def trigger():
    run()
    return {'status': 'executed'}
