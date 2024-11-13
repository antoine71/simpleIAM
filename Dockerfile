FROM python:3.13-alpine3.20 AS builder

WORKDIR /app

COPY requirements.txt .

RUN apk update && apk upgrade \
    && pip install --upgrade pip \
    && python -m venv /virtualenv \   
    && /virtualenv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.13-alpine3.20

RUN apk update && apk upgrade \
    && adduser -D appuser 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./app .
COPY --from=builder /virtualenv /virtualenv

USER appuser

CMD ["/virtualenv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]