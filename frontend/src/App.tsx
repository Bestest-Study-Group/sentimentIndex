import "./App.css";
import Header from "./components/header/header";
import { useEffect, useState } from "react";
import axios from "axios";
import SentimentChart from "./components/sentimentChart/sentimentChart";

function App() {
  const [chart, setChart] = useState(<div></div>)
  useEffect(() => {
    axios({
      method: "get",
      url: process.env.REACT_APP_REST_API + "/api/reddit",
    }).then((res) => {
      axios({
        method: 'get',
        url: process.env.REACT_APP_REST_API + '/api/news'
      }).then((news) => {
        console.log()
        setChart(<SentimentChart reddit={res.data.data[0].chart_data} news={news.data.data[0].chart_data}/>)
      })
    });
  }, []);

  return (
    <div>
      <Header sentiment="neutral" />
      {chart}
    </div>
  );
}

export default App;
