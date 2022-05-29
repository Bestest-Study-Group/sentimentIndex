import "./App.css";
import Header from "./components/header/header";
import { useEffect, useState } from "react";
import axios from "axios";
import SentimentChart from "./components/sentimentChart/sentimentChart";

function App() {
  const [chart, setChart] = useState(<div></div>)
  const [header, setHeader] = useState(<div></div>)
  const pos = ['DraftKings Inc. stock rises Wednesday, outperforms market', 'More Room For Growth In Pioneer Energy Stock?', "After Dismal Performance Last Month, L'Oreal Stock Looks Set To Rebound", 'The stock market is close to finding its bottom as corporate share buybacks surge to record highs, JPMorgan says', 'GameStop Unveils Crypto and NFT Wallet, Shares up 3%']
  const neg = ['Waste Management Inc. stock rises Thursday, still underperforms market', 'How Do You Stay Confident in a Market Crash?', "Here's 1 of the Biggest Problems With Airbnb Stock", 'Should You Buy Stocks With An Impending Bear Market And Possible Recession?', "Costco Q3 Earnings Preview: Don't Fall With It Any Longer (NASDAQ:COST)"]
  
  let pos_p = pos.map((p) => {
    return (<p>{p}</p>)
  })

  let neg_p = neg.map((n) => {
    return (<p>{n}</p>)
  })

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
        if (news.data.data[0].chart_data[0] < 0) {
          setHeader(<Header sentiment="negative"/>)
        } else {
          setHeader(<Header sentiment="positive"/>)
        }
        setChart(<SentimentChart reddit={res.data.data[0].chart_data.reverse()} news={news.data.data[0].chart_data.reverse()}/>)
      })
    });
  }, []);

  return (
    <div className='my_app'>
      {header}
      {chart}
      <div className='pos_neg'>
        <div className='pos_list'>
          <p className='pos_title'>Positive Articles</p>
          {pos_p}
        </div>
        <div className='neg_list'>
          <p className='neg_title'>Negative Articles</p>
          {neg_p}
        </div>
      </div>
    </div>
  );
}

export default App;
