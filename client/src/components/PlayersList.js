import { useOutletContext } from "react-router-dom"
import Player from "./Player"


function PlayersList(){

    const {players, deletePlayer} = useOutletContext()

    const playerComponents = players.map(player => {
        return <Player key={player.id} player={player} deletePlayer={deletePlayer} players={players}/>
    })
    return (
        <ul>{playerComponents}</ul>
    )
}

export default PlayersList