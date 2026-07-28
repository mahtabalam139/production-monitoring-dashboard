from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.multi_server_monitor import get_servers

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/servers", response_class=HTMLResponse)
def servers_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="servers.html",
        context={
            "request": request,
            "servers": get_servers()
        }
    )


@router.get("/api/servers")
def servers_api():

    return get_servers()