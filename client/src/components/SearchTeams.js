import React from "react";

function searchTeams({searchTeams, updateSearch}) {
    
    return (
        <div className="searchbar">
            <label htmlFor="search">Search Teams:</label>
            <input
            type="text"
            id="search"
            placeholder="TYPE NAME TO FIND TEAM..."
            value={searchTeams} 
            onChange={updateSearch}
            />
        </div>
    )
}

export default searchTeams