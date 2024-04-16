import React, { useEffect, useState } from "react";
// import { Outlet } from "react-router-dom";

import NavBar from "./NavBar";
import { Outlet } from "react-router-dom";



function App() {

  const [players, setPlayers] = useState([])
  const [teams, setTeams] = useState([])

  useEffect(() => {
    fetch('/players')
    .then(res => res.json())
    .then(playersData => setPlayers(playersData))
  }, [])

  useEffect(() => {
    fetch('/teams')
    .then(res => res.json())
    .then(teamsData => setTeams(teamsData))
  }, [])

  function deletePlayer(id){
    fetch(`/players/${id}`,  {
      method: "DELETE"
    })
    .then(res => {
      if(res.ok) {
        setPlayers((players) => players.filter(player => {
          return player.id !== id
        }))
      } else {
        alert("Error: Unable to Delete Player!")
      }
    })
  }
  
  return (
    <div>
      <NavBar />
      <Outlet context={{
        players: players,
        teams: teams,
        deletePlayer: deletePlayer
      }}/>
    </div>
    
  )


}

export default App;
