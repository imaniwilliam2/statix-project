// TeamInfo.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function TeamInfo() {
    const [team, setTeam] = useState(null);
    const { id } = useParams();

    useEffect(() => {
        fetch(`/teams/${id}`)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => setTeam(data))
            .catch(error => console.error('Error fetching team data:', error));
    }, [id]);

    if (!team) {
        return <div>Loading team information...</div>;
    }

    return (
        <div>
            <h1>{team.name}</h1>
            <p>Origin: {team.origin}</p>
            <p>Conference: {team.conference}</p>
            <p>Regular Season Record: {team.regularR}</p>
            <p>Playoff Record: {team.playoffR}</p>
            <p>Championships: {team.championships}</p>
            <p>Titles: {team.titles}</p>
            <p>Coach: {team.coach}</p>
            {/* Add more team information as needed */}
        </div>
    );
}

export default TeamInfo;