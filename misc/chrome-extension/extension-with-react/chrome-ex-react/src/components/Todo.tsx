import React from "react";

import "../styles/main.css";
import "../styles/todo.css";

import { getTodo, updateTodo } from "../api/todo";
import { ParseTitle, TodoModel } from "../model/todo";

export function TodoList() {
  const [todos, setTodos] = React.useState<TodoModel[]>(getTodo());

  React.useEffect(() => {
    updateTodo(todos);
  }, [todos]);

  function addTodo(title: string) {
    setTodos([...todos, new TodoModel(todos.length.toString(), title)]);
  }

  function deleteTodo(todoId: string) {
    setTodos((prevTodo) => prevTodo.filter((todo) => todo.id !== todoId));
  }

  return (
    <main id="main">
      <ul className="todo-list">
        <AddTodo addTodo={addTodo} />
        <Todo todos={todos} deleteTodo={deleteTodo} />
      </ul>
    </main>
  );
}

export function AddTodo(props: { addTodo: (title: string) => void }) {
  const todoRef = React.useRef<HTMLInputElement>(null);

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (todoRef.current === null) return;
    if (todoRef.current.value === null) return;
    props.addTodo(todoRef.current.value);
    todoRef.current.value = "";
  }

  return (
    <li className="addtodo">
      <form
        action=""
        method="get"
        id="add-form"
        onSubmit={(e) => handleSubmit(e)}
      >
        <input
          type="text"
          name="todo"
          id="todo"
          placeholder="input new todo :^)"
          ref={todoRef}
          autoFocus
        />
      </form>
    </li>
  );
}

export function Todo(props: {
  todos: TodoModel[];
  deleteTodo: (todoId: string) => void;
}) {
  function deleteTodo(todoId: string) {
    props.deleteTodo(todoId);
  }

  return (
    <>
      {props.todos.map((todo) => {
        return (
          <li
            className="todo"
            key={todo.id}
            onClick={() => deleteTodo(todo.id)}
          >
            <svg width="24" height="20" className="todo-checkbox">
              <circle
                cx="10"
                cy="11"
                r="8"
                stroke="#f8f8f8"
                fill="#2a2a2a"
                className="checkbox-circle"
              ></circle>
            </svg>
            {ParseTitle(todo.title, todo.id)}
          </li>
        );
      })}
    </>
  );
}
