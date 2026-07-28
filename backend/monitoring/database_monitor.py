import socket
import pymysql


def get_database_status():

    host = "localhost"
    port = 3306

    result = {
        "service": "MySQL",
        "host": host,
        "port": port,
        "status": "Stopped",
        "version": "-",
        "threads_connected": "-",
        "threads_running": "-"
    }

    # --------------------------------------------------
    # Check whether MySQL port is open
    # --------------------------------------------------

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    if sock.connect_ex((host, port)) != 0:
        sock.close()
        return result

    sock.close()

    # --------------------------------------------------
    # MySQL Service is running
    # --------------------------------------------------

    result["status"] = "Running"

    try:

        connection = pymysql.connect(
            host=host,
            user="root",
            password="",      # We will improve this later
            database="mysql",
            connect_timeout=2
        )

        cursor = connection.cursor()

        cursor.execute("SELECT VERSION()")
        result["version"] = cursor.fetchone()[0]

        cursor.execute("SHOW STATUS LIKE 'Threads_connected'")
        result["threads_connected"] = cursor.fetchone()[1]

        cursor.execute("SHOW STATUS LIKE 'Threads_running'")
        result["threads_running"] = cursor.fetchone()[1]

        cursor.close()
        connection.close()

    except Exception:
        pass

    return result