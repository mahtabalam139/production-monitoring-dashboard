async function updateSystem() {

    const response = await fetch("/resources");

    const data = await response.json();

    document.getElementById("cpu_usage").innerHTML =
        data.cpu_percent + " %";

    document.getElementById("memory_usage").innerHTML =
        data.memory_percent + " %";

    document.getElementById("cpu_bar").style.width =
        data.cpu_percent + "%";

    document.getElementById("memory_bar").style.width =
        data.memory_percent + "%";

}

updateSystem();

setInterval(updateSystem,5000);