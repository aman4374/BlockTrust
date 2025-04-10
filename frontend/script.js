function startSimulation() {
  const progressBar = document.getElementById("progressBar");
  progressBar.style.width = "0%";

  fetch("http://127.0.0.1:5000/simulate")
    .then((response) => response.json())
    .then((data) => {
      progressBar.style.width = "100%";
      renderResults(data);
      renderChart(data);
    });
}

function renderResults(data) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  data.forEach((round, index) => {
    const roundDiv = document.createElement("div");
    roundDiv.classList.add("round");

    const roundTitle = document.createElement("h3");
    roundTitle.innerText = `Round ${index + 1}`;
    roundDiv.appendChild(roundTitle);

    round.forEach((node) => {
      const nodeDiv = document.createElement("div");
      nodeDiv.classList.add("node");
      nodeDiv.innerText = `Node ${node.id} | Action: ${node.action} | Trust: ${node.trust_score} | Rep: ${node.reputation} | Penalty: ${node.penalty}`;
      roundDiv.appendChild(nodeDiv);
    });

    resultsDiv.appendChild(roundDiv);
  });
}

function renderChart(data) {
  const ctx = document.getElementById("trustChart").getContext("2d");
  const numNodes = data[0].length;

  const trustData = Array(numNodes).fill(0).map(() => []);
  const labels = data.map((_, i) => `R${i + 1}`);

  data.forEach((round) => {
    round.forEach((node, idx) => {
      trustData[idx].push(node.trust_score);
    });
  });

  const colors = [
    "#3b82f6", "#22c55e", "#f97316", "#e11d48",
    "#8b5cf6", "#10b981", "#facc15", "#14b8a6",
    "#ec4899", "#6366f1"
  ];

  const datasets = trustData.map((trust, idx) => ({
    label: `Node ${idx}`,
    data: trust,
    borderColor: colors[idx % colors.length],
    fill: false,
    tension: 0.2,
  }));

  if (window.trustChartInstance) {
    window.trustChartInstance.destroy();
  }

  window.trustChartInstance = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: datasets,
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
        title: {
          display: true,
          text: "Trust Score Over Time",
        },
      },
    },
  });
}

function downloadCSV() {
  window.location.href = "http://127.0.0.1:5000/download_csv";
}
