import { useState } from "react";
import { Link } from "react-router-dom";
import TeamStats from "./TeamStats";


function Team({team}){

    const [favorite, setFavorite] = useState(team.favorite)
    const [showTeamStats, setShowTeamStats] = useState(false);

    function toggleHeart() {
        console.log(team)

        fetch(`/teams/${team.id}`, {
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

    function toggleTeamStats() {
        setShowTeamStats(!showTeamStats); // Toggle visibility
    }

    return (
        <div className="team">
            <img src={team.image} alt={team.name}/>
            <h2><Link to={`/teams/${team.id}`}>{team.name}</Link></h2> 
            <div className="team-buttons">
            {likeButton}
            <button onClick={toggleTeamStats}>
                {showTeamStats ? "Hide Stats" : "Show Stats"} 
                </button>
            {showTeamStats && <TeamStats teamId={team.id} />}
            </div>
        </div>
    )
}

export default Team;