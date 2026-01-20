from fastapi import APIRouter,Request
import logging
logger = logging.getLogger(__name__)
router=APIRouter(
    prefix="/health",
    tags=["Health"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def health_check(request:Request):
    logger.info(f"You went to {request.url.path}")
    return {"status": "ok"}