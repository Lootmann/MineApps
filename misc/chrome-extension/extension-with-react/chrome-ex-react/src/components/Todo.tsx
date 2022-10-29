import React from "react";

import "../styles/todo.css";

export function TodoList() {
  return (
    <ul className="todo-list">
      <AddTodo />
      <Todo />
    </ul>
  );
}

export function Todo() {
  return <li className="todo">Todo</li>;
}

export function AddTodo() {
  return <li className="addtodo">AddTodo</li>;
}
