import json, os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.user_controller import router as UserController
from app.controller.auth_controller import router as AuthController

app = FastAPI()

origins = json.loads(os.getenv("ORIGINS", "[]"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/health')
def health_check():
    return True

app.include_router(UserController)
app.include_router(AuthController)