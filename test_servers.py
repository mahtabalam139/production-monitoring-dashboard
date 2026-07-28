from backend.monitoring.multi_server_monitor import get_servers

servers = get_servers()

for server in servers:
    print(server)