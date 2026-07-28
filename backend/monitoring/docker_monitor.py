import docker


def get_docker_summary():

    try:

        client = docker.from_env()

        running = client.containers.list()

        all_containers = client.containers.list(all=True)

        container_list = []

        for container in all_containers:

            ports = "-"

            if container.attrs["NetworkSettings"]["Ports"]:

                ports = ", ".join(container.attrs["NetworkSettings"]["Ports"].keys())

            container_list.append({

                "name": container.name,

                "image": container.image.tags[0] if container.image.tags else "Unknown",

                "status": container.status,

                "ports": ports

            })

        return {

            "engine": "Running",

            "running": len(running),

            "stopped": len(all_containers) - len(running),

            "images": len(client.images.list()),

            "volumes": len(client.volumes.list()),

            "networks": len(client.networks.list()),

            "containers": container_list

        }

    except Exception as e:

        return {

            "engine": "Disconnected",

            "running": 0,

            "stopped": 0,

            "images": 0,

            "volumes": 0,

            "networks": 0,

            "containers": [],

            "error": str(e)

        }