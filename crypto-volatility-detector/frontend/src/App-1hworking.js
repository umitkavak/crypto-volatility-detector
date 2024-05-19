import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/api/data')
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
        setError('There was an error fetching the data.');
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  // Ensure data is not null before accessing its properties
  if (!data) {
    return <div>No data available</div>;
  }

  return (
    <div>
      <h1>Crypto Volatility Detector</h1>
      <h2>Cryptocurrency Data (sorted by 1-minute change):</h2>
      <ul>
        {data.map((item, index) => (
          <li key={index}>
            <h3>{item.name} ({item.symbol.toUpperCase()})</h3>
            <p>Current Price: ${item.current_price}</p>
            <p>Market Cap: ${item.market_cap}</p>
            <p>1h Change: {item.price_change_percentage_1h_in_currency}%</p>
            <p>24h Change: {item.price_change_percentage_24h}%</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
