/**
 * todo.ts
 *
 * when save to google chrome.storage,
 * convert array(Todo[]) to JSON
 *
 * when load from google chorme.storage,
 * convert JSON to array(Todo[])
 */

import { TodoModel } from "../model/todo";

function getTestTodo() {
  return JSON.stringify([
    new TodoModel("0", "Why"),
    new TodoModel("1", "Hello"),
    new TodoModel("2", "Friend"),
    new TodoModel("3", ":^)"),
  ]);
}

export function getTodo(): TodoModel[] {
  console.log(">>> getTodo");
  const ls = localStorage.getItem("testKey");
  console.log(`localStorage = ${ls}`);

  const todos: TodoModel[] = [];

  const json = JSON.parse(getTestTodo());
  for (const obj of json) {
    todos.push(new TodoModel(obj.id, obj.title));
  }

  return todos;
}

export function updateTodo() {
  localStorage.setItem("testKey", "hoge");

  const json = JSON.stringify({ hello: "world" });
}
