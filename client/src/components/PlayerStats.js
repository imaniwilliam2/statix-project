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
        <div className='player-stats'>
            <ul>
                <li>GP: {playerStats.gp}</li>
                <li>MPG: {playerStats.minpg}</li>
                <li>RPG: {playerStats.rebpg}</li>
                <li>PPG: {playerStats.ppg}</li>
                <li>APG: {playerStats.apg}</li>
                <li>SPG: {playerStats.spg}</li>
                <li>BPG: {playerStats.bpg}</li>
                <li>TPG: {playerStats.tpg}</li>
                <li>FG%: {playerStats.fgpercentage}</li>
                <li>3P%: {playerStats.threepercentage}</li>
                {/* Add more stats as needed */}
            </ul>
        </div>
    );
}

export default PlayerStats;
