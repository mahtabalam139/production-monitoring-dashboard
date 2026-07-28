from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.log_monitor import get_logs

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/logs", response_class=HTMLResponse)
def logs_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="logs.html",
        context={
            "request": request,
            "logs": get_logs()
        }
    )


@router.get("/api/logs")
def logs_api():

    return get_logs()