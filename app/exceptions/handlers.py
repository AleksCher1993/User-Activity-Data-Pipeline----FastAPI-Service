import logging
from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from app.exceptions.custom import (ExternalServiceUnavailable,DataProcessingError)

logger=logging.getLogger(__name__)


def register_exception_handlers(app:FastAPI):
    @app.exception_handler(ExternalServiceUnavailable)
    async def external_service_handler(
        request:Request,exc:ExternalServiceUnavailable
    ):
        logger.error(f"External service error: {exc}")
        return JSONResponse(
            status_code=503,
            content={
                "detail":"External service is unavailable",
                "path":request.url.path,
            }
        )

    @app.exception_handler(DataProcessingError)
    async def data_processing_error_handler(
        request:Request,exc:DataProcessingError
    ):
        logger.error(f"Processing error: {exc}")
        return JSONResponse(
            status_code=500,
            content={
                "detail":"Internal data processing error",
                "path":request.url.path,
            })
        