import { useOutletContext } from "react-router-dom"


function MyTeam(){

    const { myTeamPlayers, deleteFromTeam } = useOutletContext()
    

    function handleDelete(id) {
        deleteFromTeam(id)
    }



    return(
        <>
        <div className="my-team-container">
            <ul className="my-team-list">
                {myTeamPlayers.map((player) => (
                    <li className="my-team-players" key={player.id}>
                        <img className="my-team-img" src={player.image} alt={player.name}/>
                        <h1>{player.name}</h1>
                        <button className="cut-button" onClick={() => handleDelete(player.id)}>Cut</button>
                    </li>
                ))}
            </ul>
        </div>
       </>
    )
}
export default MyTeam