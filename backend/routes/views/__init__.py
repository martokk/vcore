from fastapi import APIRouter

from backend.routes.views.jobs import job_scheduler, jobs
from backend.routes.views.login import login
from backend.routes.views.root import root
from backend.routes.views.user import user


# Views router
vcore_views_router = APIRouter(include_in_schema=False)
vcore_views_router.include_router(root.router, tags=["Root"])
vcore_views_router.include_router(login.router, tags=["Logins"])
vcore_views_router.include_router(user.router, tags=["Users"])

vcore_views_router.include_router(jobs.router, tags=["Jobs"])
vcore_views_router.include_router(job_scheduler.router, tags=["Job Schedulers"])
