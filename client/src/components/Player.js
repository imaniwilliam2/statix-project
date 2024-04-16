import { useState } from "react";


function Player({player, deletePlayer, players}){

    const [favorite, setFavorite] = useState(player.favorite)

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
            setFavorite(players, data);
        })

        setFavorite(!favorite)
    }

    const likeButton = favorite ? <button className="like-button" onClick={toggleHeart}>❤️</button> : <button className="like-button" onClick={toggleHeart}>♡</button> ;



    function handleDeleteButton(){
        deletePlayer(player.id)
    }

    return (
        <div>
            <img src={player.image} alt={player.name}/>
            <h1>{player.name}</h1>
            {likeButton}
            <button className="delete-button" onClick={handleDeleteButton}>Delete Player</button>
        </div>
    )
}

export default Player;