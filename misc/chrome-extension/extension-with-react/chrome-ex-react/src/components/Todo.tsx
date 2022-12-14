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
    const maxTodoId = todos.reduce(
      (op, item) => (op = op > item.id ? op : item.id),
      0
    );
    console.log(maxTodoId);
    setTodos([...todos, new TodoModel(maxTodoId + 1, title)]);
  }

  function deleteTodo(todoId: number) {
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
          placeholder="  input new todo :^)"
          ref={todoRef}
          autoFocus
        />
      </form>
    </li>
  );
}

export function Todo(props: {
  todos: TodoModel[];
  deleteTodo: (todoId: number) => void;
}) {
  function deleteTodo(todoId: number) {
    props.deleteTodo(todoId);
  }

  return (
    <>
      {props.todos.length === 0 ? (
        <li className="no-todo" key="0">
          No Todo Here!
          <br />
          Great Work!
          <br />
          You can create new one :^)
        </li>
      ) : (
        props.todos.map((todo) => {
          return (
            <li className="todo" key={todo.id}>
              <svg
                width="24"
                height="20"
                className="todo-checkbox"
                onClick={() => deleteTodo(todo.id)}
              >
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
        })
      )}
    </>
  );
}
