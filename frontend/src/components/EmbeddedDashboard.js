import React, { useState, useEffect } from 'react';

export default function EmbeddedDashboard() {
  const url = "http://192.168.0.105:1880/ui/#!/0?socketid=5xXtEo921g4GPqxDAAAB";
  const [error, setError] = useState(null);

  useEffect(() => {
    const iframe = document.querySelector('iframe');
    iframe.addEventListener('error', (event) => {
      setError('Error loading dashboard');
    });
  }, []);

  return (
    <div style={{border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f0f0f0'}}>
      <h2 style={{color: '#00698f'}}>Embedded Dashboard</h2>
      {error ? (
        <div style={{color: 'red'}}>{error}</div>
      ) : (
        <iframe 
          src={url} 
          title="Embedded Dashboard" 
          style={{width: '100%', height: '500px', border: 'none'}}
        ></iframe>
      )}
    </div>
  );
}