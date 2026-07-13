from fastapi import APIRouter

from backend.monitoring.resource_monitor import get_resource_usage

router = APIRouter()


@router.get("/resources")
def resources():
    return get_resource_usage()