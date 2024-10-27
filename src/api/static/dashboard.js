function fetchMetrics() {
    fetch("/metrics", { method: "GET" })
    .then(response => response.json())
    .then(data => {
        document.getElementById("cpu-usage").innerText = data.cpu_usage || '--';
        document.getElementById("memory-usage").innerText = data.memory_usage || '--';
        document.getElementById("request-count").innerText = data.request_count || '--';
    })
    .catch(error => console.error("Error fetching metrics:", error));
}

// Fetch metrics every 5 seconds automatically
setInterval(fetchMetrics, 5000);
