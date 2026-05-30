FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# IMPORTANT: use  for Render
CMD ["sh", "-c", "uvicorn api.server:app --host 0.0.0.0 --port \"]
