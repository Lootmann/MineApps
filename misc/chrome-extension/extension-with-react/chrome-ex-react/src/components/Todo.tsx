import React from "react";

import "../styles/todo.css";
import { getTodo } from "../api/todo";
import { TodoModel } from "../model/todo";

export function TodoList() {
  const [todos, setTodos] = React.useState<TodoModel[]>(getTodo());

  function addTodo(title: string) {
    setTodos([...todos, new TodoModel(todos.length.toString(), title)]);
  }

  return (
    <ul className="todo-list">
      <AddTodo addTodo={addTodo} />
      <Todo todos={todos} />
    </ul>
  );
}

type AddTodoProps = {
  addTodo: (title: string) => void;
};

export function AddTodo(props: AddTodoProps) {
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

type TodoProps = {
  todos: TodoModel[];
};

export function Todo(props: TodoProps) {
  return (
    <>
      {props.todos.map((todo) => {
        return (
          <li className="todo" key={todo.id}>
            {todo.title}
          </li>
        );
      })}
    </>
  );
}
