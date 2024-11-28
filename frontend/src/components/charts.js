import React from "react";
import { Line, Pie } from "react-chartjs-2";

export function LineChart({ data, labels, title }) {
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: title,
        data: data,
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.4,
      },
    ],
  };

  return <Line data={chartData} />;
}

export function PieChart({ data, labels, title }) {
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: title,
        data: data,
        backgroundColor: ["#ff6384", "#36a2eb", "#ffce56"],
        hoverOffset: 4,
      },
    ],
  };

  return <Pie data={chartData} />;
}
