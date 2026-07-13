from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.system_info import get_system_info
from backend.monitoring.resource_monitor import get_resource_usage

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    resource_data = get_resource_usage()
    system_data = get_system_info()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "request": request,
            "resource": resource_data,
            "system": system_data
        }
    )