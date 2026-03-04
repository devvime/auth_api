from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def create_user(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Home page",
        "message": "Hello, World! 🚀"
    })