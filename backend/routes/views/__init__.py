from fastapi import APIRouter

from app.routes.views.dashboard import dashboard
from vcore.backend.routes.views.jobs import job_scheduler, jobs
from vcore.backend.routes.views.login import login
from vcore.backend.routes.views.user import user


# Root routes
root_router = APIRouter()
root_router.include_router(login.router, tags=["Logins"])
root_router.include_router(user.router, tags=["Users"])

root_router.include_router(jobs.router, tags=["Jobs"])
root_router.include_router(job_scheduler.router, tags=["Job Schedulers"])

# Views router
vcore_views_router = APIRouter(include_in_schema=False)
vcore_views_router.include_router(root_router)
vcore_views_router.include_router(dashboard.router, tags=["Dashboard"])
