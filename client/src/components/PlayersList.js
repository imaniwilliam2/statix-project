import { useOutletContext } from "react-router-dom"
import Player from "./Player"
import { Link } from "react-router-dom";
import Search from "./Search";
import { useState } from "react";




function PlayersList(){
    const [searchPlayers, setSearchPlayers] = useState("")
    const {players, deletePlayer, addToMyTeam } = useOutletContext()


    const filteredPlayers = players.filter(player => {
        if(searchPlayers === "") return true
        return player.name.toUpperCase().includes(searchPlayers.toUpperCase())
    })

    function updateSearch(e) {
        setSearchPlayers(e.target.value)
    }



    const playerComponents = filteredPlayers.map(player => {
        return <Player key={player.id} player={player} deletePlayer={deletePlayer} players={players} addToMyTeam={addToMyTeam}/>
    })
    return (
        <>
            <Search updateSearch={updateSearch} searchPlayers={searchPlayers}/>
            <Link className="form" to={"/players-form"}>Add A Player</Link>
            <ul className="players">{playerComponents}</ul>
        </>
    )
}

export default PlayersList