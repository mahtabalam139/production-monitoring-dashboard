# ============================================================
# Imports
# ============================================================

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.home import router as home_router
from backend.api.system import router as system_router
from backend.api.resources import router as resources_router
from backend.api.dashboard import router as dashboard_router
from backend.api.system_page import router as system_page_router

# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="Production Monitoring Dashboard",
    description="Enterprise Monitoring System",
    version="1.0.0"
)

# ============================================================
# Static Files
# ============================================================

app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# ============================================================
# Register Routers
# ============================================================

app.include_router(home_router)
app.include_router(system_router)
app.include_router(resources_router)
app.include_router(dashboard_router)
app.include_router(system_page_router)