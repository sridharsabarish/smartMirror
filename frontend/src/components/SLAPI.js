
import React, { useState, useEffect } from 'react';

export default function SLAPI(){
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
    <div style={{border: '1px solid #333', borderRadius: '5px', padding: '10px', margin: '10px', backgroundColor: '#2f3640'}}>
      {groupedDepartures && Object.entries(groupedDepartures).map(([direction, displays]) => (
        <div key={direction} style={{marginBottom: '10px', display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
          <p style={{margin: 0, fontWeight: 'bold', fontSize: '1.2em', color: '#FFA500', backgroundColor: '#1a202c', padding: '5px', borderRadius: '5px'}}>{direction}</p>
          {displays.map((display, index) => (
            <p key={index} style={{margin: 0, paddingLeft: '10px', fontSize: '1em', color: index !=0 ? '#808080' : '#00BFFF'  }}> {display} </p>
          ))}
        </div>
      ))}
    </div>
  );


}
