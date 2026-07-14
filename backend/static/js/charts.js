// ======================================================
// CPU & Memory Charts
// ======================================================

// Keep only last 20 values
const MAX_POINTS = 20;

// Arrays
let cpuData = [];
let memoryData = [];
let labels = [];

// CPU Chart
const cpuChart = new Chart(
    document.getElementById("cpuChart"),
    {
        type: "line",

        data: {
            labels: labels,

            datasets: [

                {
                    label: "CPU %",
                    data: cpuData,

                    borderColor: "#20c997",

                    backgroundColor: "rgba(32,201,151,.15)",

                    tension: .35,

                    fill: true

                }

            ]
        },

        options: {

            responsive: true,

            animation: false,

            scales: {

                y: {

                    min: 0,

                    max: 100

                }

            }

        }

    }
);

// Memory Chart
const memoryChart = new Chart(
    document.getElementById("memoryChart"),
    {
        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Memory %",

                    data: memoryData,

                    borderColor: "#0dcaf0",

                    backgroundColor: "rgba(13,202,240,.15)",

                    tension: .35,

                    fill: true

                }

            ]

        },

        options: {

            responsive: true,

            animation: false,

            scales: {

                y: {

                    min: 0,

                    max: 100

                }

            }

        }

    }
);


// Update Charts Every 5 Seconds

async function updateCharts() {

    const response = await fetch("/resources");

    const data = await response.json();

    const now = new Date().toLocaleTimeString();

    labels.push(now);

    cpuData.push(data.cpu_percent);

    memoryData.push(data.memory_percent);

    if (labels.length > MAX_POINTS) {

        labels.shift();

        cpuData.shift();

        memoryData.shift();

    }

    cpuChart.update();

    memoryChart.update();

}

updateCharts();

setInterval(updateCharts, 5000);