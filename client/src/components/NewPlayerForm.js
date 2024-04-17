import { useState } from "react";
import { useOutletContext, useNavigate } from "react-router-dom";

function NewPlayerForm(){

    const [form, setForm] = useState({
        name: "",
        height: "",
        weight: "",
        team: "",
        number: "",
        image: "",
        birthday: "",
        bio: "",
        drafted: "",
        position: ""
    })

    const {addPlayer} = useOutletContext()
    const navigate = useNavigate()

    function updateForm(event){
        setForm({...form, [event.target.name]: event.target.value})
    }

    function handleSubmit(event){
        event.preventDefault()
        
        addPlayer(form)

        setForm({
        name: "",
        height: "",
        weight: "",
        team: "",
        number: "",
        image: "",
        birthday: "",
        bio: "",
        drafted: "",
        position: ""
        })
        navigate('/players')
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>Add A Player</h1>
            <input onChange={updateForm} type="text" name="name" placeholder="Player Name" value={form.name} required/>
            <input onChange={updateForm} type="text" name="height" placeholder="Height" value={form.height} required/>
            <input onChange={updateForm} type="text" name="weight" placeholder="Weight" value={form.weight} required/>
            <input onChange={updateForm} type="text" name="team" placeholder="Team" value={form.team} required/>
            <input onChange={updateForm} type="text" name="number" placeholder="Number" value={form.number} required/>
            <input onChange={updateForm} type="text" name="image" placeholder="Image URL" value={form.image} required/>
            <input onChange={updateForm} type="text" name="birthday" placeholder="Birthday" value={form.birthday} required/>
            <input onChange={updateForm} type="text" name="bio" placeholder="Bio" value={form.bio} required/>
            <input onChange={updateForm} type="text" name="drafted" placeholder="Drafted" value={form.drafted} required/>
            <input onChange={updateForm} type="text" name="position" placeholder="Position" value={form.position} required/>
            <input type="submit" value="Add Player"/>
        </form>
    )


}

export default NewPlayerForm