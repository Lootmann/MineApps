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

const STORAGE_KEY = "todoStorage";

export function getTodo(): TodoModel[] {
  console.log(">>> getTodo");
  const storage = localStorage.getItem(STORAGE_KEY);

  if (storage === null) {
    return [];
  }

  const todos: TodoModel[] = [];
  for (const obj of JSON.parse(storage)) {
    todos.push(new TodoModel(obj.id, obj.title));
  }
  return todos;
}

export function updateTodo(todos: TodoModel[]) {
  console.log(">>> updateTodo");
  localStorage.removeItem(STORAGE_KEY);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
}
