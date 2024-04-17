import React from "react";

function Search({searchPlayers, updateSearch}) {
    
    return (
        <div className="searchbar">
            <label htmlFor="search">Search Players:</label>
            <input
            type="text"
            id="search"
            placeholder="Type name to find sneaker..."
            value={searchPlayers} 
            onChange={updateSearch}
            />
        </div>
    )
}

export default Search