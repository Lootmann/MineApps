import React from "react";
import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

import "./styles/index.css";
import { App } from "./components/App";
import { ErrorPage } from "./components/ErrorPage";

import { Canvas } from "./components/Canvas";
import { Circle } from "./scripts/test";
import { Hoge } from "./scripts/hoge";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/test",
        element: <Canvas sketch={Circle} />,
      },
      {
        path: "/hoge",
        element: <Canvas sketch={Hoge} />,
      },
    ],
  },
]);

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

reportWebVitals();
