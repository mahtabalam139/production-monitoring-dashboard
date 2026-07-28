from backend.monitoring.log_monitor import write_log
from backend.monitoring.log_monitor import get_logs

write_log("INFO", "Dashboard Started")
write_log("INFO", "CPU Usage Updated")
write_log("WARNING", "Memory Usage High")
write_log("ERROR", "Docker Engine Disconnected")

print(get_logs())