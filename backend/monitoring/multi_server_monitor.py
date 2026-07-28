import random


def get_servers():

    return [

        {
            "name": "Production-01",
            "ip": "10.10.10.11",
            "cpu": round(random.uniform(10, 60), 1),
            "memory": round(random.uniform(40, 90), 1),
            "disk": round(random.uniform(20, 70), 1),
            "status": "Running"
        },

        {
            "name": "Production-02",
            "ip": "10.10.10.12",
            "cpu": round(random.uniform(10, 60), 1),
            "memory": round(random.uniform(40, 90), 1),
            "disk": round(random.uniform(20, 70), 1),
            "status": "Running"
        },

        {
            "name": "UAT-01",
            "ip": "10.10.20.11",
            "cpu": round(random.uniform(10, 60), 1),
            "memory": round(random.uniform(40, 90), 1),
            "disk": round(random.uniform(20, 70), 1),
            "status": "Running"
        },

        {
            "name": "Docker-Host",
            "ip": "10.10.30.21",
            "cpu": round(random.uniform(10, 60), 1),
            "memory": round(random.uniform(40, 90), 1),
            "disk": round(random.uniform(20, 70), 1),
            "status": "Running"
        }

    ]