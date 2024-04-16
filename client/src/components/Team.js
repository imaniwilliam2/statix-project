function Team({team}){
    return (
        <div>
            <img src={team.image} alt={team.name}/>
            <h1>{team.name}</h1>
        </div>
    )
}

export default Team;