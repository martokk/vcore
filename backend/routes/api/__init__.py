from fastapi import APIRouter

from backend.routes.api.v1.endpoints import job_queue_ws, job_scheduler, users
from backend.routes.api.v1.endpoints.job_queue import router as job_queue_router


vcore_api_router = APIRouter()

# Job Queue Routes
vcore_api_router.include_router(job_queue_router, tags=["Job Queue"])
vcore_api_router.include_router(job_queue_ws.router, tags=["Job Queue WS"])
vcore_api_router.include_router(job_scheduler.router, tags=["Job Schedulers"])

# Users Routes
vcore_api_router.include_router(users.router, tags=["Users"])
