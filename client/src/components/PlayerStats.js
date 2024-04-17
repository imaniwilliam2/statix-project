// In a new component file (e.g., PlayerStats.js)

import React, { useState, useEffect } from 'react';

function PlayerStats({ playerId }) {
    const [playerStats, setPlayerStats] = useState(null);

    useEffect(() => {
        fetch(`/players/${playerId}/stats`)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => setPlayerStats(data))
            .catch(error => console.error('Error fetching player stats:', error));
    }, [playerId]);

    if (!playerStats) {
        return <div>Loading player stats...</div>;
    }

    return (
        <div>
            <ul>
                <h2>GP: {playerStats.gp}</h2><li>MPG: {playerStats.minpg}</li><li>RPG: {playerStats.rebpg}</li>
                {/* Add more stats as needed */}
            </ul>
        </div>
    );
}

export default PlayerStats;
