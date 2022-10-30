import React from "react";
import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";

import "./styles/variables.css";
import "./index.css";
import { TodoList } from "./components/Todo";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

root.render(
  <React.StrictMode>
    <TodoList />
  </React.StrictMode>
);

reportWebVitals();
