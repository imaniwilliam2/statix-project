import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';


function TeamInfo() {
    const [team, setTeam] = useState(null);
    const [players, setPlayers] = useState([]);
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
        
        fetch(`/teams/${id}/players`)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => setPlayers(data))
            .catch(error => console.error('Error fetching team players:', error));
    }, [id]);

    if (!team) {
        return <div>Loading team information...</div>;
    }

    return (
        <div className='team-info'>
            <img className='mx-auto' src={team.image} alt={team.name} />
            <h1>{team.name}</h1>
            <p>Origin: {team.origin}</p>
            <p>Conference: {team.conference}</p>
            <p>Regular Season Record: {team.regularR}</p>
            <p>Playoff Record: {team.playoffR}</p>
            <p>Championships: {team.championships}</p>
            <p>Titles: {team.titles}</p>
            <p>Coach: {team.coach}</p>
            
            <div>
                {players.length === 0 ? (
                    <div></div>
                ) : (
                    <div>
                        <h1 className='team-players-info-h1' >Team Players</h1>
                    <ul className='team-players-info'>
                        {players.map(player => (
                            <li key={player.id}>
                                <Link to={`/players/${player.id}`}> <strong>{player.name}</strong> </Link>
                            </li>
                        ))}
                    </ul>
                    </div>
                )}
            </div>
        </div>
    );
}

export default TeamInfo;
