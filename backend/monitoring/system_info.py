import platform
import socket
import os

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.release(),
        "python_version": platform.python_version(),
        "processor": platform.processor(),
        "architecture": platform.machine(),
        "cpu_count": os.cpu_count()
    }