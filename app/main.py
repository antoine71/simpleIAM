from routers import user
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    return {"ping": "ok"}


app.include_router(user.router, prefix="/users", tags=["Users"])
