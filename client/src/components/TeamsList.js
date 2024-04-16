import { useOutletContext } from "react-router-dom"
import Team from "./Team"


function TeamsList(){

    const {teams} = useOutletContext()

    const teamsComponents = teams.map(team => {
        return <Team key={team.id} team={team}/>
    })
    return (
        <ul>{teamsComponents}</ul>
    )
}

export default TeamsList