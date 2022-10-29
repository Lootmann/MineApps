import React from "react";

import "../styles/todo.css";

export function TodoList() {
  const [todos, setTodos] = React.useState<string[]>(["prev", "todo", "next"]);

  return (
    <ul className="todo-list">
      <AddTodo />
      <Todo todos={todos} />
    </ul>
  );
}

export function AddTodo() {
  const todoRef = React.useRef(null);

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
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

type TodoProps = {
  todos: string[];
};

export function Todo(props: TodoProps) {
  return (
    <>
      {props.todos.map((todo) => {
        return (
          <li className="todo" key={todo}>
            {todo}
          </li>
        );
      })}
    </>
  );
}
