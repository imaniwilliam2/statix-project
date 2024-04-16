import { useOutletContext } from "react-router-dom"
import Player from "./Player"
// import NewPlayerForm from "./NewPlayerForm";
import { Link } from "react-router-dom";



function PlayersList(){

    const {players, deletePlayer} = useOutletContext()

    const playerComponents = players.map(player => {
        return <Player key={player.id} player={player} deletePlayer={deletePlayer} players={players}/>
    })
    return (
        <>
            <Link className="form" to={"/players-form"}>Add A Player</Link>
            <ul>{playerComponents}</ul>
        </>
    )
}

export default PlayersList