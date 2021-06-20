import os, sys

import uvicorn
from fastapi import FastAPI
from routers.healthcheck import Healthcheck
from routers.login import Login

path = os.path.dirname(os.path.abspath(__file__))  # NOQA
sys.path.append(path)  # NOQA

app = FastAPI()

app.include_router(Healthcheck.router, prefix="/healthcheck")
app.include_router(Login.router, prefix="/login")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)