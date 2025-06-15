import React, { useState, useEffect } from 'react';

export default function Poem()
{

  const url = "https://poetrydb.org/author/Shakespeare"
const [poems, setPoems] = useState(null);
const [lines, setLines] = useState(null);
const [title, setTitle] = useState(null);
useEffect(() => {
  fetch(url)
  .then(response => response.json())
   .then((poems) => {
            console.log(poems);
            setPoems(poems);
            const randomIndex = Math.floor(Math.random() * poems.length);
            setLines(poems[randomIndex]['lines'])
            setTitle(poems[randomIndex]['title'])
         })
 },[url])


const linesItems = lines && lines.map(line => <li>{line}</li>);


  return (
    <div style={{borderRadius: '10px', padding: '20px', margin: '20px', backgroundColor: '#fafafa', color: '#333'}}>
      <h1 style={{textAlign: 'center', marginBottom: '15px'}}> {title} </h1>
      {lines && <ol style={{listStyleType: 'decimal', paddingLeft: '25px'}}>
        {lines.map(line => <li key={line} style={{marginBottom: '8px', color: '#444'}}>{line}</li>)}
      </ol>}
    </div>
  );

  
}



