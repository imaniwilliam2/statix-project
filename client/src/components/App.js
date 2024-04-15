import React, { useEffect, useState } from "react";
// import { Outlet } from "react-router-dom";

import NavBar from "./NavBar";
import { Outlet } from "react-router-dom";



function App() {

  const [players, setPlayers] = useState([])

  useEffect(() => {
    fetch('/players')
    .then(res => res.json())
    .then(playersData => setPlayers(playersData))
  }, [])

  
  return (
    <div>
      <NavBar />
      <Outlet context={{
        players: players
      }}/>
    </div>
    
  )


}

export default App;
