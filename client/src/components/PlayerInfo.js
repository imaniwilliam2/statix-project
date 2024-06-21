import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom"

function PlayerInfo() {
    const [player, setPlayer] = useState(null)

    const { id } = useParams(); 
    
   
    useEffect(() => {
        fetch(`/players/${id}`)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error("Network response was not ok.");
            })
            .then(data => setPlayer(data))
            .catch(error => console.error("Error fetching player data:", error));
    }, [id]); 

    if (!player) {
        return <div>Loading player information...</div>;
    }

    return (
        <div className="player-info">
            <img className="mx-auto" src={player.image} alt={player.name} />
            <h2>{player.name}</h2>
            <p>Height: {player.height}</p>
            <p>Weight: {player.weight}lb</p>
            <p>Number: #{player.number}</p>
            <p>Birthday: {player.birthday}</p>
            <p>Drafted: {player.drafted}</p>
            <p>Position: {player.position}</p>
            <p className="text-center max-w-lg mx-auto">Bio: {player.bio}</p>

        </div>
    );
}

export default PlayerInfo;
