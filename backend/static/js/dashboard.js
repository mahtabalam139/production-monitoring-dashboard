// ======================================================
// Dashboard Live Monitoring
// ======================================================

async function updateResources() {

    try {

        const response = await fetch("/resources");

        const data = await response.json();

        // Update Values
        document.getElementById("cpu_usage").innerHTML =
            data.cpu_percent + " %";

        document.getElementById("memory_usage").innerHTML =
            data.memory_percent + " %";

        document.getElementById("disk_usage").innerHTML =
            data.disk_percent + " %";

        // Update Progress Bars
        document.getElementById("cpu_bar").style.width =
            data.cpu_percent + "%";

        document.getElementById("memory_bar").style.width =
            data.memory_percent + "%";

        document.getElementById("disk_bar").style.width =
            data.disk_percent + "%";
    }
    catch (error) {
        console.error(error);
    }
}
updateResources();
setInterval(updateResources, 5000);