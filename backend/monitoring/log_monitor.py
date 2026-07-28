import os
from datetime import datetime

LOG_FILE = "logs/application.log"


def get_logs():

    if not os.path.exists(LOG_FILE):
        return []

    logs = []

    with open(LOG_FILE, "r", encoding="utf-8") as file:

        for line in file.readlines():

            line = line.strip()

            if not line:
                continue

            parts = line.split("|")

            if len(parts) != 3:
                continue

            logs.append({
                "time": parts[0],
                "level": parts[1],
                "message": parts[2]
            })

    logs.reverse()

    return logs


def write_log(level, message):

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"{now}|{level}|{message}\n")