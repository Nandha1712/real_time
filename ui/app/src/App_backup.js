import './App.css';
import { useState, useEffect } from 'react';

const apiCall = {
  event: 'bts:subscribe',
  data: { channel: 'order_book_btcusd' },
};

function App() {
  const [bids, setBids] = useState([{"user": "initial", "msg": "000"}]);

  useEffect(() => {
    console.log("*****************")

    // const ws = new WebSocket('wss://ws.bitstamp.net');
    const ws = new WebSocket('ws://127.0.0.1:5000/test');
    ws.onopen = (event) => {
      ws.send(JSON.stringify(apiCall));
    };
    
    ws.onmessage = function (event) {
      console.log("On message => ", event);
      // const json = JSON.parse(event.data);
      // try {
      //   if ((json.event === 'data')) {
      //     console.log("Prev Bids", bids);
      //     let newBids = json.data.bids.slice(0, 5);
      //     console.log("New Bids", newBids);
      //     setBids([...bids, ...newBids]);
      //   }
      // } catch (err) {
      //   console.log(err);
      // }
    };
    //clean up function
    return () => ws.close();
  }, []);

  const firstBids = bids.map((item, index) => (
    <div key={index}>
      <p> {item}</p>
    </div>
  ));

  return <div>{firstBids}</div>;
}

export default App;
