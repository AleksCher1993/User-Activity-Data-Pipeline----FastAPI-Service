
from fastapi import FastAPI
from fastapi.responses import FileResponse
import logging

from app.utils.logger import logger_init
from app.services.processor import (
    get_users as get_users_service, 
    get_posts as get_posts_service,
    get_users_activity as get_users_activity_service)

logger_init()
logger=logging.getLogger(__name__)

app = FastAPI()
# root endpoint serving static files
@app.get("/")
def root():
    return FileResponse("app/public/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}
# users endpoints
@app.get("/users")
def get_users_endpoint():
    return get_users_service()
@app.get("/users/activity")
def get_user_activity_endpoint():
    users = get_users_service()
    posts = get_posts_service()
    return get_users_activity_service(users, posts)

# posts endpoints
@app.get("/posts")
def get_posts_endpoint():
    return get_posts_service()

