from fastapi import APIRouter

from backend.monitoring.system_info import get_system_info

router = APIRouter()


@router.get("/system")
def system_info():
    return get_system_info()