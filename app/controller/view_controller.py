from fastapi import APIRouter, Request, Depends
from fastapi_limiter.depends import RateLimiter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.shared.rate_limit import global_rate_limit

router = APIRouter(dependencies=[global_rate_limit])

templates = Jinja2Templates(directory="client/html")

@router.get("/", response_class=HTMLResponse)
async def create_user(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "Home page",
        "message": "Hello, World! 🚀"
    })