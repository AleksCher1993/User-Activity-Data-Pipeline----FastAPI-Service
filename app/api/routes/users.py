import logging
from typing import List
from app.core.dependencies import UserActivityService, get_user_activity_service
from fastapi import APIRouter, Query, Depends

from app.models.schemas import UserActivity
logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def get_users_endpoint(services:UserActivityService=Depends(get_user_activity_service)):
    return services.get_users()

@router.get("/activity",response_model=List[UserActivity])
def get_user_activity_endpoint(services:UserActivityService=Depends(get_user_activity_service)):
    return services.get_users_activity()

@router.get("/activity/top",response_model=List[UserActivity])
def get_user_activity_top_endpoint(service:UserActivityService=Depends(get_user_activity_service),limit:int= Query(gt=0,le=50)):
    return service.get_top_activity(limit)