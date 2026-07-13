from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "application": "Production Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }