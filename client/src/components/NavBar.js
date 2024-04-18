import {NavLink} from 'react-router-dom';
import { Link } from 'react-router-dom';

function NavBar(){
    return (
        <>
        <Link to="/" className='header'><h1>STATIX</h1></Link>
        <h1 className='season'>2023-24 Season</h1>
        <nav className='nav-bar'>
            <NavLink to="/players">Players</NavLink>
            <NavLink to="/teams">Teams</NavLink>
            <NavLink to="/my-team">My Team</NavLink>
        </nav>
        </>
    )
}

export default NavBar;