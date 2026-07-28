import psutil


def get_processes():

    process_list = []

    for process in psutil.process_iter(
        ['pid', 'name', 'memory_info']
    ):

        try:

            process_list.append({

                "pid": process.info["pid"],

                "name": process.info["name"] or "Unknown",

                "cpu": round(process.cpu_percent(interval=None), 1),

                "memory": round(
                    process.info["memory_info"].rss / (1024 * 1024),
                    2
                ),

                "status": "Running"

            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):

            continue

    process_list.sort(
        key=lambda x: x["cpu"],
        reverse=True
    )

    return process_list[:20]