// ======================================================
// Live Resource Monitoring
// ======================================================

async function updateResources() {

    try {

        const response = await fetch("/resources");

        const data = await response.json();

        document.getElementById("cpu_usage").innerHTML =
            data.cpu_percent + " %";

        document.getElementById("memory_usage").innerHTML =
            data.memory_percent + " %";

        document.getElementById("disk_usage").innerHTML =
            data.disk_percent + " %";

    }

    catch (error) {

        console.error("Unable to fetch monitoring data.", error);

    }

}

// Update every 5 seconds
setInterval(updateResources, 5000);

// First update after page loads
updateResources();