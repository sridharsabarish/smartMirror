
import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';


import Gallery from './Gallery.js';
import Poem from './components/Poem.js'
import SLAPI from './components/SLAPI.js'
import DateTime from './components/DateTime.js'
import EmbeddedDashboard from './components/EmbeddedDashboard.js'
import Overdue from './components/Overdue.js'


// Untested
import RSS from './components/Rss.js';  


// Understand how to fetch a json using REACT





function App() {



  return (
    <section style={{background: 'linear-gradient(to bottom, #032B44, #1A202C)', height: '100vh'}}> 
      <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'space-around', height: '100%'}}>

        <SLAPI style={{flex:3, minWidth: '300px', maxWidth: '500px'}}/>
        <div  style={{display:'flex', justifyContent: 'space-around'}}> 
          <Poem style={{flex:2, minWidth: '300px', maxWidth: '500px'}}/>
          <EmbeddedDashboard style={{flex:3, minWidth: '500px', maxWidth: '800px'}}/>
          <Overdue/>
          <RSS style={{flex:3, minWidth: '500px', maxWidth: '800px'}}/>
        </div>
        <DateTime  style={{flex:2, minWidth: '300px', maxWidth: '500px'}} />
        
      </div>
    </section>
);
  }
export default App;

