from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.docker_monitor import get_docker_summary

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/docker", response_class=HTMLResponse)
def docker_dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="docker.html",
        context={
            "request": request,
            "docker": get_docker_summary()
        }
    )


@router.get("/api/docker")
def docker_api():

    return get_docker_summary()