import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";
import PlayerStats from "./PlayerStats";


function Player({player, deletePlayer, addToMyTeam}){

    const [favorite, setFavorite] = useState(player.favorite)
    const [showPlayerStats, setShowPlayerStats] = useState(false)

    const navigate = useNavigate()


    function toggleHeart() {
        console.log(player)

        fetch(`/players/${player.id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ 
                favorite: !favorite }) 
        })
        .then(res => res.json())
        .then(data => {
            setFavorite(data.favorite);
        })

        setFavorite(!favorite)
    }

    const likeButton = favorite ? <button className="like-button" onClick={toggleHeart}>❤️</button> : <button className="like-button" onClick={toggleHeart}>♡</button> ;



    function handleDeleteButton(){
        deletePlayer(player.id)
    }

    function handleAddToTeam() {
        addToMyTeam(player)
        navigate('/my-team')
    }

    function togglePlayerStats() {
        setShowPlayerStats(!showPlayerStats); // Toggle visibility
    }

    return (
        <div>
            <img src={player.image} alt={player.name}/>
            <h2><Link to={`/players/${player.id}`}>{player.name}</Link></h2>
            {likeButton}
            <button className="delete-button" onClick={handleDeleteButton}>X</button>
            <button className="add-button" onClick={handleAddToTeam}>Draft To My Team</button>
            <button onClick={togglePlayerStats}>
                {showPlayerStats ? "Hide Stats" : "Show Stats"}
            </button>
            {showPlayerStats && <PlayerStats playerId={player.id} />}
        </div>
    )
}

export default Player;