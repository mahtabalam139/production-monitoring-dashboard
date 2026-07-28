// ======================================================
// Process Monitoring
// ======================================================

let processData = [];
let sortBy = "cpu";

// ------------------------------------------------------
// Load & Refresh Processes
// ------------------------------------------------------

async function refreshProcesses() {

    const response = await fetch("/api/processes");

    processData = await response.json();

    // Sort according to selected column
    processData.sort((a, b) => b[sortBy] - a[sortBy]);

    let rows = "";

    processData.forEach(process => {

        let cpuClass = "";
        let memoryClass = "";

        if (process.cpu >= 70) {
            cpuClass = "text-danger fw-bold";
        }

        if (process.memory >= 500) {
            memoryClass = "text-warning fw-bold";
        }

        rows += `
            <tr>

                <td>${process.pid}</td>

                <td>${process.name}</td>

                <td class="${cpuClass}">
                    ${process.cpu}
                </td>

                <td class="${memoryClass}">
                    ${process.memory}
                </td>

                <td>
                    <span class="badge rounded-pill bg-success">
                        ${process.status}
                    </span>
                </td>

            </tr>
        `;
    });

    document.getElementById("processTable").innerHTML = rows;

    document.getElementById("processCount").innerHTML = processData.length;

    document.getElementById("lastUpdated").innerHTML =
        new Date().toLocaleTimeString();
}

// ------------------------------------------------------
// Initial Load
// ------------------------------------------------------

refreshProcesses();

setInterval(refreshProcesses, 5000);

// ------------------------------------------------------
// Search
// ------------------------------------------------------

document.getElementById("searchBox").addEventListener("keyup", function () {

    let value = this.value.toLowerCase();

    let rows = document.querySelectorAll("#processTable tr");

    rows.forEach(row => {

        row.style.display =
            row.innerText.toLowerCase().includes(value)
                ? ""
                : "none";

    });

});

// ------------------------------------------------------
// Sorting
// ------------------------------------------------------

document.getElementById("sortCpu").addEventListener("click", function () {

    sortBy = "cpu";

    refreshProcesses();

});

document.getElementById("sortMemory").addEventListener("click", function () {

    sortBy = "memory";

    refreshProcesses();

});