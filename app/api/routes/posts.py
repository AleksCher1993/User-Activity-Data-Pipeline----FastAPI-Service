
from app.core.dependencies import UserActivityService, get_user_activity_service
from fastapi import APIRouter, Depends


router=APIRouter(
    prefix="/posts",
    tags=["Posts"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def get_posts_endpoint(service:UserActivityService=Depends(get_user_activity_service)):
    return service.get_posts()