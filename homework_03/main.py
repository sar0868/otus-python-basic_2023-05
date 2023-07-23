from fastapi import FastAPI
from view import router as ping_router

app = FastAPI()
app.include_router(ping_router, prefix="/ping")


@app.get("/")
def index():
    return {"message": "not found"}

