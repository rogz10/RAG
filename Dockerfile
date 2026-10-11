FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# torch version cpu
RUN pip install torch==2.13.0 --index-url https://download.pytorch.org/whl/cpu

# dépendances copiées  pour profiter du cache docker
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 8000

# 0.0.0.0  pour que l api soit joignable hors du conteneur
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
