import uvicorn

from fastapi import FastAPI, APIRouter
from controllers import UserController, LoginController
from core.config import settings

app = FastAPI()

api_router = APIRouter()

api_router.include_router(UserController.router, prefix="/users", tags=["users"])
api_router.include_router(LoginController.router, prefix="/login", tags=["users"])

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
