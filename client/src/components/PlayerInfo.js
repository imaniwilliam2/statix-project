// PlayerInfo.js

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
    }, []); 

    if (!player) {
        return <div>Loading player information...</div>;
    }

    return (
        <div>
            <img src={player.image} alt={player.name} />
            <h2>{player.name}</h2>
            <p>Height: {player.height}</p>
            <p>Weight: {player.weight}</p>
            <p>Team: {player.team}</p>
            {/* Add more player information as needed */}
        </div>
    );
}

export default PlayerInfo;
