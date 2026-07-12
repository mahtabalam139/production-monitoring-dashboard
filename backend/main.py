from fastapi import FastAPI

# Create FastAPI application
app = FastAPI(
    title="Production Monitoring Dashboard",
    description="Enterprise Monitoring System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "application": "Production Monitoring Dashboard",
        "status": "Running",
        "version": "1.0.0"
    }