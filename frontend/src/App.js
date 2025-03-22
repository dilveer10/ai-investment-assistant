import React, { useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function App() {
  const [symbol, setSymbol] = useState('');
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchStockData = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:5000/stock/${symbol}`);
      if (response.data.prices) {
        // Reverse data so the latest day is on the right
        const sorted = [...response.data.prices].reverse();
        setData(sorted);
      } else {
        alert('Invalid symbol or no data found.');
      }
    } catch (error) {
      console.error(error);
      alert('Error fetching stock data');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>📈 AI Investment Assistant</h1>
      <input
        value={symbol}
        onChange={(e) => setSymbol(e.target.value)}
        placeholder="Enter Stock Symbol (e.g., AAPL)"
        style={{ padding: '0.5rem', fontSize: '1rem' }}
      />
      <button onClick={fetchStockData} style={{ marginLeft: '1rem', padding: '0.5rem 1rem' }}>
        Get Data
      </button>

      {loading && <p>Loading...</p>}

      {data.length > 0 && (
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis domain={['auto', 'auto']} />
            <Tooltip />
            <Line type="monotone" dataKey="close" stroke="#8884d8" strokeWidth={2} />
          </LineChart>
        </ResponsiveContainer>
      )}
    </div>
  );
}

export default App;
