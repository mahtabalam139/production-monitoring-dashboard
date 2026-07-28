from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.process_monitor import get_processes

router = APIRouter()

templates = Jinja2Templates(
    directory="backend/templates"
)


@router.get("/processes", response_class=HTMLResponse)
def processes(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="process.html",

        context={

            "request": request,

            "processes": get_processes()

        }

    )
@router.get("/api/processes")
def process_api():

    return get_processes()