
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
//Todo :Potential to refactor the fetcher code

function DateTime() {

  const date = new Date();
  const current_time = date.toLocaleTimeString();
  const date_today = date.toLocaleDateString();

  return (
    <div >
    <p >
        Last updated: {current_time}, {date_today}
    </p>
</div>
  );
}



function EmbeddedDashboard() {
  const url = "http://192.168.0.107:1880/ui/#!/0?socketid=5xXtEo921g4GPqxDAAAB";
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
function Overdue(){
  //const url ="https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100"
  const url = "http://192.168.0.101:5000/inventory/overdue"
  const [data, setData] = useState(null);
    useEffect(() => {
      fetch(url)
        .then(response => response.json())
        .then(data => setData(data));
    }, [url]);
  
    const inventory = data?.inventory || {};
    const items = Object.values(inventory).map(item => (
      <div key={item.id}>
        <p>{item.name}</p>
      </div>
    ));
  
    return (
      <div style={{border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f0f0f0'}}>
        <h2 style={{color: '#00698f'}}>Overdue</h2>
        {items}
      </div>
    );
  
  
  }
function SLAPI(){
  const url = "https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100";
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => setData(data.departures));
  }, [url]);

  const groupedDepartures = data?.reduce((acc, departure) => {
    if (!acc[departure.direction]) {
      acc[departure.direction] = [];
    }
    acc[departure.direction].push(departure.display);
    return acc;
  }, {});

  return (
    <div style={{border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f7d202'}}>
      {groupedDepartures && Object.entries(groupedDepartures).map(([direction, displays]) => (
        <div key={direction} style={{marginBottom: '10px'}}>
          <p style={{margin: 0, fontWeight: 'bold'}}>{direction}</p>
          {displays.map((display, index) => (
            <p key={index} style={{margin: 0, paddingLeft: '10px'}}>{display}</p>
          ))}
        </div>
      ))}
    </div>
  );


}




function App() {
  return (
 <section> 
  <div>
    {/* <SLAPI style={{flex:3}}/> */}
<EmbeddedDashboard/>
  <DateTime />
  </div>
  </section>
);
  }
export default App;

