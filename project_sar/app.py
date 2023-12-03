from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from ceramics import router as ceramics_router

app = FastAPI()
app.include_router(ceramics_router, prefix="/ceramics")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def get_index(request: Request):
    return templates.TemplateResponse(
        name="base.html",
        context={
            "request": request,
        },
    )
