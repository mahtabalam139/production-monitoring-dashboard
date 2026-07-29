from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/")
def home():
    return RedirectResponse(url="/dashboard")

@router.get("/health")
def health():
    return {
        "application": "Production Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }
