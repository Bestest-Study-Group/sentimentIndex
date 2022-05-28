import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
function SentimentChart() {
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

  const labels = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
  ];
  const options = {
    spanGaps: true,
  };
  const data = {
    labels,
    datasets: [
      {
        label: "Dataset 1",
        data: [1, 2, undefined, 4, 5, 6, 7],
        borderColor: "rgb(250, 177, 49)",
        backgroundColor: "rgb(250, 177, 49)",
      },
      {
        label: "Dataset 2",
        data: [-1, -2, -3, -4, -5, -6, -7],
        borderColor: "rgb(55, 118, 116",
        backgroundColor: "rgb(211, 227, 222)",
      },
    ],
  };

  return <Line options={options} data={data} />;
}
export default SentimentChart;
