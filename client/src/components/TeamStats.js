// TeamStats.js
import React, { useState, useEffect } from 'react';

function TeamStats({ teamId }) {
    const [teamStats, setTeamStats] = useState(null);

    useEffect(() => {
        fetch(`/teams/${teamId}/stats`)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => setTeamStats(data))
            .catch(error => console.error('Error fetching team stats:', error));
    }, [teamId]);


    if (!teamStats) {
        return <div>Loading team stats...</div>;
    }

    return (
        <div>
            
                <ul>
                    <li>Wins: {teamStats.wins}</li>
                    <li>Loses: {teamStats.loses}</li>
                    {/* Add more stats as needed */}
                </ul>
            
        </div>
    );
}

export default TeamStats;
