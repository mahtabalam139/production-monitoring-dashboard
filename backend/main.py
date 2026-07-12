from fastapi import FastAPI
from backend.monitoring.system_info import get_system_info
from backend.monitoring.resource_monitor import get_resource_usage

# Create FastAPI application
app = FastAPI(
    title="Production Monitoring Dashboard",
    description="Enterprise Monitoring System",
    version="1.0.0"
)
@app.get("/system")
def system_info():
    return get_system_info()
@app.get("/resources")
def resources():
    return get_resource_usage()

@app.get("/")
def home():
    return {
        "application": "Production Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }