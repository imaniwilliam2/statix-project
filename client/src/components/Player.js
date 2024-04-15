function Player({player}){
    return (
        <div>
            <img src={player.image} alt={player.name}/>
            <h1>{player.name}</h1>
        </div>
    )
}

export default Player;