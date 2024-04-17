import { useState } from "react";


function Team({team}){

    const [favorite, setFavorite] = useState(team.favorite)


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


    return (
        <div>
            <img src={team.image} alt={team.name}/>
            <h1>{team.name}</h1> {likeButton}
        </div>
    )
}

export default Team;