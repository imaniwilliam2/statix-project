import React from "react";

import App from "./components/App";
import ErrorPage from "./components/ErrorPage";
import Home from "./components/Home";
import PlayersList from "./components/PlayersList"
import Teams from "./components/Teams"
import MyTeam from "./components/MyTeam";



import "./index.css";
import { createRoot } from "react-dom/client";

import { createBrowserRouter, RouterProvider } from "react-router-dom";



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
                element: <Teams />
            },
            {
                path:"/my-team",
                element: <MyTeam />

            }
        ]
    }
])


const container = document.getElementById("root");
const root = createRoot(container);
root.render(<RouterProvider router={router}/>);
