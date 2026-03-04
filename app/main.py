import json, os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.controller.view_controller import router as ViewController
from app.controller.user_controller import router as UserController
from app.controller.auth_controller import router as AuthController

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=json.loads(os.getenv("ORIGINS", "[]")),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(ViewController)
app.include_router(AuthController)
app.include_router(UserController)