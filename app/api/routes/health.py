from fastapi import APIRouter
import logging
logger = logging.getLogger(__name__)
router=APIRouter(
    prefix="/health",
    tags=["Health"],
    responses={404:{"description":"Not found"}}
)

@router.get("/")
def health_check():
    return {"status": "ok"}