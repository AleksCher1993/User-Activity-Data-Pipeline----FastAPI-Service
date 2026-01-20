from fastapi import APIRouter,Depends
from app.core.dependencies import get_health_service
from app.services.health import HealthService

router=APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("/dependencies")
def get_posts_endpoint(service:HealthService=Depends(get_health_service)):
    return {
        "status":"ok",
        "dependencies":service.check(),
    }