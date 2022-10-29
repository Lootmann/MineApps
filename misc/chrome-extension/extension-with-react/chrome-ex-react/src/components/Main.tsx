import React from "react";
import "../styles/main.css";
import { Todo, AddTodo } from "./Todo";

export function Main() {
  const renderTodo = (): React.ReactNode => {
    return <Todo />;
  };

  return (
    <main id="main">
      <ul className="todo-list">
        <AddTodo />
        {renderTodo()}
      </ul>
    </main>
  );
}
