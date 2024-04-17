import {NavLink} from 'react-router-dom';
import { Link } from 'react-router-dom';

function NavBar(){
    return (
        <nav>
            <Link to="/"><h1>STATIX</h1></Link>
            <NavLink to="/">Home</NavLink>
            <NavLink to="/players">Players</NavLink>
            <NavLink to="/teams">Teams</NavLink>
            <NavLink to="/my-team">My Team</NavLink>
        </nav>
    )
}

export default NavBar;