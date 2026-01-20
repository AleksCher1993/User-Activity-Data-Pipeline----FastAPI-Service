
from fastapi import FastAPI
from fastapi.responses import FileResponse
import logging
from app.utils.logger import logger_init
from app.api.routes import health,users,posts
from app.middleware.timing import timing_middleware
from app.exceptions.handlers import register_exception_handlers
logger_init()
logger=logging.getLogger(__name__)

app = FastAPI()
app.middleware("http")(timing_middleware)
register_exception_handlers(app)


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(health.router)
@app.get("/")
def get_root():

    return FileResponse("app/public/index.html")




