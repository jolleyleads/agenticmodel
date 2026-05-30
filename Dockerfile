FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Render-safe: avoid sh parsing completely
CMD ["uvicorn", "api.server:app", "--host", "0.0.0.0", "--port", "10000"]
