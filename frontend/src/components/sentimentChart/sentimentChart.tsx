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
function SentimentChart(props: any) {
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );

  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

  const temps = [1,2,3,4,5,6].reverse();
  let labels = temps.map((temp) => {
    let days = (new Date()).getTime() - (temp * 24 * 60 * 60 * 1000)
    let point_date = new Date(days)
    return ((months[point_date.getMonth()] + " " + (point_date.getDate())))
  })
  const colorCode = 'black';
  const defaultFont = {
    family: "Georgia",
    size: 16,
    color: 'black'
  }
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
        data: props.reddit.slice(props.reddit.length - 6, props.reddit.length),
        borderColor: "rgb(250, 177, 49)",
        backgroundColor: "rgb(250, 177, 49)",
      },
      {
        label: "Media",
        data: props.news.slice(props.news.length - 6, props.news.length),
        borderColor: "rgb(55, 118, 116",
        backgroundColor: "rgb(211, 227, 222)",
      },
    ],
  };

  return <Line options={options} data={data} />;
}
export default SentimentChart;
