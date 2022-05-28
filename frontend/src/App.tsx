import "./App.css";
import Header from "./components/header/header";
import { useEffect } from "react";
import axios from "axios";

function App() {
  useEffect(() => {
    axios({
      method: "get",
      url: process.env.REACT_APP_REST_API + "/api/reddit",
    }).then((res) => {
      console.log(res.data);
    });
  }, []);
  return (
    <div>
      <Header sentiment="neutral" />
    </div>
  );
}

export default App;
