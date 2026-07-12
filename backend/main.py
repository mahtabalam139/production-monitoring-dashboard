# ============================================================
# Imports
# ============================================================

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from backend.monitoring.system_info import get_system_info
from backend.monitoring.resource_monitor import get_resource_usage

# ============================================================
# FastAPI Application
# ============================================================
app = FastAPI(
    title="Production Monitoring Dashboard",
    description="Enterprise Monitoring System",
    version="1.0.0"
)
# ============================================================
# Templates & Static Files
# ============================================================
templates = Jinja2Templates(directory="backend/templates")
app.mount("/static", StaticFiles(directory="backend/static"), name="static")


@app.get("/")
def home():
    return {
        "application": "Production Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/system")
def system_info():
    return get_system_info()


@app.get("/resources")
def resources():
    return get_resource_usage()


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    data = get_resource_usage()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request, "data": data}
    )