from fastapi import FastAPI
from .api.v1.routes import router

app = FastAPI(title="Flowboard API", version="1.0.0")

app.include_router(router, prefix="")
