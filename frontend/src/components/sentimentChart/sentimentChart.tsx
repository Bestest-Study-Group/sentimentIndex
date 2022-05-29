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

  const colorCode = 'black';
  const defaultFont = {
    family: "Georgia",
    size: 16,
    color: 'black'
  }

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
    scales: {
      x: {
        grid: {
          
        },
        beginAtZero: false,
        ticks: {
          color: colorCode,
          font: defaultFont
        }
      },
      y: {
        grid: {
          
        },
        beginAtZero: true,
        ticks: {
          color: colorCode,
          font: defaultFont
        }
      }
    },
    plugins: {
      legend: {
          labels: {
              color: colorCode,
              font: defaultFont
          }
      },
  }
  };
  const data = {
    labels,
    datasets: [
      {
        label: "Reddit",
        data: [1, 2, undefined, 4, 5, 6, 7],
        borderColor: "rgb(250, 177, 49)",
        backgroundColor: "rgb(250, 177, 49)",
      },
      {
        label: "Media",
        data: [-1, -2, -3, -4, -5, -6, -7],
        borderColor: "rgb(55, 118, 116",
        backgroundColor: "rgb(211, 227, 222)",
      },
    ],
  };

  return <Line options={options} data={data} />;
}
export default SentimentChart;
