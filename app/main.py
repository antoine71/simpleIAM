from fastapi import FastAPI
from api.routes import user

app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "ok"}


app.include_router(user.router, prefix="/users", tags=["Users"])