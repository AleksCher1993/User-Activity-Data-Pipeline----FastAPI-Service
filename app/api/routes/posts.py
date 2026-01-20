import logging
from app.core.dependencies import UserActivityService, get_user_activity_service
from fastapi import APIRouter, Depends, Request
logger = logging.getLogger(__name__)

router=APIRouter(
    prefix="/posts",
    tags=["Posts"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def get_posts_endpoint(request:Request,service:UserActivityService=Depends(get_user_activity_service)):
    logger.info(f"You went to {request.url.path}")
    return service.get_posts()