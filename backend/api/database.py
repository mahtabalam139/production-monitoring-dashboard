from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.monitoring.database_monitor import get_database_status

router = APIRouter()

templates = Jinja2Templates(directory="backend/templates")


@router.get("/database", response_class=HTMLResponse)
def database_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="database.html",
        context={
            "request": request,
            "database": get_database_status()
        }
    )


@router.get("/api/database")
def database_api():

    return get_database_status()