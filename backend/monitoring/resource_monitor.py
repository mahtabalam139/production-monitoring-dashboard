import psutil


def get_resource_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_used_gb": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "memory_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "disk_percent": psutil.disk_usage("/").percent,
        "disk_used_gb": round(psutil.disk_usage("/").used / (1024 ** 3), 2),
        "disk_total_gb": round(psutil.disk_usage("/").total / (1024 ** 3), 2),
    }