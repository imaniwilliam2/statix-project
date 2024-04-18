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
        <div className='team-stats'>
                <ul>
                    <li>Wins: {teamStats.wins}</li>
                    <li>Loses: {teamStats.loses}</li>
                    <li>Conference Standing: {teamStats.cstanding}</li>
                    <li>Points: {teamStats.points}</li>
                    <li>Assists: {teamStats.assists}</li>
                    <li>Rebounds: {teamStats.rebounds}</li>
                </ul>
            
        </div>
    );
}

export default TeamStats;
