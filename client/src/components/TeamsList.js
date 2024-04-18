import { useOutletContext } from "react-router-dom"
import Team from "./Team"
import SearchTeams from "./SearchTeams";
import { useState } from "react";



function TeamsList(){
    const [searchTeams, setSearchTeams] = useState("")

    const {teams} = useOutletContext()

    const filteredTeams = teams.filter(team => {
        if(searchTeams === "") return true
        return team.name.toUpperCase().includes(searchTeams.toUpperCase())
    })

    function updateSearch(e) {
        setSearchTeams(e.target.value)
    }


    const teamsComponents = filteredTeams.map(team => {
        return <Team key={team.id} team={team}/>
    })
    return (
        < div className="teams">
            <SearchTeams updateSearch={updateSearch} searchTeams={searchTeams}/>
            <ul className="teams-list">{teamsComponents}</ul>
        </div>
    )
}

export default TeamsList