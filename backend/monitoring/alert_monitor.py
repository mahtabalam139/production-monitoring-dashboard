from backend.monitoring.resource_monitor import get_resource_usage
from backend.monitoring.docker_monitor import get_docker_summary


def get_alerts():

    alerts = []

    resources = get_resource_usage()
    docker = get_docker_summary()

    # ---------------- CPU ----------------

    if resources["cpu_percent"] >= 80:
        alerts.append({
            "level": "Critical",
            "message": f"CPU Usage High ({resources['cpu_percent']}%)"
        })

    # ---------------- Memory ----------------

    if resources["memory_percent"] >= 80:
        alerts.append({
            "level": "Warning",
            "message": f"Memory Usage High ({resources['memory_percent']}%)"
        })

    # ---------------- Disk ----------------

    if resources["disk_percent"] >= 90:
        alerts.append({
            "level": "Critical",
            "message": f"Disk Usage High ({resources['disk_percent']}%)"
        })

    # ---------------- Docker ----------------

    if docker["engine"] != "Running":
        alerts.append({
            "level": "Critical",
            "message": "Docker Engine Down"
        })

    # ---------------- No Alerts ----------------

    if len(alerts) == 0:
        alerts.append({
            "level": "Healthy",
            "message": "All Systems Operational"
        })

    return alerts