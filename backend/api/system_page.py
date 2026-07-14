from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.system_info import get_system_info
from backend.monitoring.resource_monitor import get_resource_usage

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/system-page", response_class=HTMLResponse)
def system_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="system.html",
        context={
            "request": request,
            "system": get_system_info(),
            "resource": get_resource_usage()
        }
    )