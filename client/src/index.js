import React from "react";

import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import Home from "./components/Home";
import PlayersList from "./components/PlayersList"
import TeamsList from "./components/TeamsList"
import MyTeam from "./components/MyTeam";




import "./index.css";
import { createRoot } from "react-dom/client";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import NewPlayerForm from "./components/NewPlayerForm";
import PlayerStats from "./components/PlayerStats";
import PlayerInfo from "./components/PlayerInfo";



const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/players",
                element: <PlayersList />
            },
            {
                path: "/teams",
                element: <TeamsList />
            },
            {
                path:"/my-team",
                element: <MyTeam />

            },
            {
                path: "/players-form",
                element: <NewPlayerForm />
            },
            {
                path: "/players/:id/stats",
                element: <PlayerStats />
            },
            {
                path: "/players/:id",
                element: <PlayerInfo />
            }
        ]
    }
])


const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router={router}/>);
