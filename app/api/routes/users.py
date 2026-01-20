import logging
from typing import List
from app.core.dependencies import UserActivityService, get_user_activity_service
from fastapi import APIRouter, Query, Depends,Request

from app.models.schemas import UserActivity
logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def get_users_endpoint(request:Request,services:UserActivityService=Depends(get_user_activity_service)):
    logger.info(f"You went to {request.url.path}")
    return services.get_users()

@router.get("/activity",response_model=List[UserActivity])
def get_user_activity_endpoint(request:Request,services:UserActivityService=Depends(get_user_activity_service)):
    logger.info(f"You went to {request.url.path}")
    return services.get_users_activity()

@router.get("/activity/top",response_model=List[UserActivity])
def get_user_activity_top_endpoint(request:Request,service:UserActivityService=Depends(get_user_activity_service),limit:int= Query(gt=0,le=50)):
    logger.info(f"You went to {request.url.path}")
    return service.get_top_activity(limit)