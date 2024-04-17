import React, { useEffect, useState } from "react";

import NavBar from "./NavBar";
import { Outlet } from "react-router-dom";



function App() {

  const [players, setPlayers] = useState([])
  const [teams, setTeams] = useState([])
  const [myTeamPlayers, setMyTeamPlayers] = useState([])

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

  useEffect(() => {
    fetch('/my-team')
    .then(res => res.json())
    .then(myTeamData => setMyTeamPlayers(myTeamData) )
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

  function addPlayer(newPlayerData){
  fetch('/players', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(newPlayerData)
  })
  .then(response => {
    if(response.ok) {
      return response.json(); 
    } else {
      throw new Error('Network response was not ok.'); 
    }
  })
  .then(newPlayerData => {

    setPlayers(prevPlayers => [...prevPlayers, newPlayerData]); 
  })
  .catch(error => {
    alert("Error: " + error.message);
  });
}

function addToMyTeam(player){
  fetch(`/my-team`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(player)
  })
  .then(res => res.json())
  .then(teamDetails => setMyTeamPlayers(team => [...team, teamDetails]))
}

function deleteFromTeam(id) {
  fetch(`/my-team/${id}`, {
    method: "DELETE"
  })
  .then(res => {
    if(res.ok) {
      setMyTeamPlayers((myTeamPlayers) => myTeamPlayers.filter(team_players => {
        return team_players.id !== id
      }))
    }else {
      alert("Error: Unable To Delete Sneaker!")
    }
  })
}

  
  return (
    <div>
      <NavBar />
      <Outlet context={{
        players: players,
        teams: teams,
        deletePlayer: deletePlayer,
        addPlayer: addPlayer,
        addToMyTeam: addToMyTeam,
        myTeamPlayers: myTeamPlayers,
        deleteFromTeam: deleteFromTeam
      }}/>
    </div>
    
  )


}

export default App;
