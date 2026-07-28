from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.alert_monitor import get_alerts

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/alerts", response_class=HTMLResponse)
def alerts_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="alerts.html",
        context={
            "request": request,
            "alerts": get_alerts()
        }
    )


@router.get("/api/alerts")
def alerts_api():

    return get_alerts()