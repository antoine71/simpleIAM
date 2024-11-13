FROM python:3.13-alpine3.20 AS builder

WORKDIR /app

COPY requirements.txt .

RUN apk update && apk upgrade \
    && apk add --no-cache \
        cargo \
        gcc \
        libffi-dev \
        make \
        musl-dev \
        openssl-dev \
    && pip install --upgrade pip \
    && pip install virtualenv \
    && python -m virtualenv /virtualenv \
    && source /virtualenv/bin/activate \    
    && pip install --no-cache-dir -r requirements.txt


FROM python:3.13-alpine3.20

RUN apk update && apk upgrade \
    && addgroup --gid 5000 appgroup \
    && adduser --uid 5000 \
    --ingroup appgroup \
    --disabled-password \
    --no-create-home \
    appuser 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./app .
COPY --from=builder /virtualenv /virtualenv

USER appuser

EXPOSE 8003

CMD ["/virtualenv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]