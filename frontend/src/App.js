
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

// TODO : Potential to refactor the fetcher code

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



function Overdue(){
  //const url ="https://transport.integration.sl.se/v1/sites/5502/departures?forecast=100"
  const url = "http://192.168.0.102:5000/inventory/overdue"
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
    <div style={{border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f0f0f0'}}>
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




function WeatherClothingSuggestion() {
  const [weather, setWeather] = useState(null);
  const [suggestion, setSuggestion] = useState('');

  useEffect(() => {
    const url = 'http://api.weatherapi.com/v1/current.json?key=ca6db37f82fc4cba9cf51956241909&q=Stockholm';
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setWeather(data.current);
        const temp = data.current.temp_c;
        if (temp < 5) {
          setSuggestion('3 layers');
        } else if (temp < 10) {
          setSuggestion('Heavy Jacket!');
        } else if (temp < 20) {
          setSuggestion('Autumn Jacket');
        } else {
          setSuggestion('A t-shirt should be fine.');
        }
      });
  }, []);

  return (
    <div style={{border: '1px solid black', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#f0f0f0'}}>
      <h2 style={{color: '#00698f'}}>Weather Clothing Suggestion</h2>
      {weather && (
        <div>
          <p>Temperature: {weather.temp_c}°C</p>
          <p>{suggestion}</p>
        </div>
      )}
    </div>
  );
}


function App() {
  return (
 <section> 
  <div style={{display: 'flex', flexDirection: 'column'}}>
    <SLAPI style={{flex:3}}/>
 
 

  <div style={{display: 'flex', flexDirection: 'row'}}>
  <Overdue style={{flex: 1}}/>
  <WeatherClothingSuggestion/>
  <DateTime />

  </div>
  </div>
  </section>
);
  }
export default App;

