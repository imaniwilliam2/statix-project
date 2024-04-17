import { useState } from "react";
import { useNavigate } from "react-router-dom";


function Player({player, deletePlayer, players, addToMyTeam}){

    const [favorite, setFavorite] = useState(player.favorite)

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

    return (
        <div>
            <img src={player.image} alt={player.name}/>
            <h1>{player.name}</h1>
            {likeButton}
            <button className="delete-button" onClick={handleDeleteButton}>Delete Player</button>
            <button className="add-button" onClick={handleAddToTeam}>Add To My Team</button>
        </div>
    )
}

export default Player;