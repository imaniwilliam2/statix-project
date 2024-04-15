import {NavLink} from 'react-router-dom';

function NavBar(){
    return (
        <nav>
            <h1>STATIX</h1>
            <NavLink to="/">Home</NavLink>
            <NavLink to="/players">Players</NavLink>
            <NavLink to="/teams">Teams</NavLink>
            <NavLink to="/my-team">My Team</NavLink>
        </nav>
    )
}

export default NavBar;