import time
import logging
from fastapi import Request

logger = logging.getLogger(__name__)

async def timing_middleware(request:Request, call_next):
    start_time=time.perf_counter()
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    
    process_time=time.perf_counter()-start_time
    response.headers["X-Process-Time"]=f"{process_time:.4f}"
    
    logger.info(
        f"Completed request: {request.method} {request.url.path} "
        f"| {process_time:.4f} ms | {response.status_code}"
    )
    return response