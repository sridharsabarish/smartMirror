import React, { useState, useEffect } from "react";
export default function Overdue() {
  const url = "http://192.168.0.101:5000/inventory/overdue";
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setData(data))
      .catch(error => setError(error));
  }, [url]);

  const inventory = data?.inventory || {};
  const items = Object.values(inventory).map(item => (
    <div key={item.id}>
      <p>{item.name}</p>
    </div>
  ));

  return (
    <div style={{ border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f0f0f0' }}>
      <h2 style={{ color: '#00698f' }}>Overdue</h2>
      {error ? <p style={{ color: 'red' }}>{error.message}</p> : items}
    </div>
  );
}

