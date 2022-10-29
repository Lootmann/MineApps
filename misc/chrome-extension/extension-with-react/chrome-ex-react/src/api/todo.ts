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

export function getTodo(): TodoModel[] {
  // chrome.storage.sync.get(["todo"], function (todo) {
  //   console.log(todo);
  // });
  return [
    new TodoModel("1", "Why"),
    new TodoModel("2", "Hello"),
    new TodoModel("3", "Friend"),
    new TodoModel("4", ":^)"),
  ];
}

export function updateTodo(id: number) {
  const json = JSON.stringify({ hello: "world" });
  chrome.storage.sync.set({ todos: json }, function () {
    console.log(`value is set to 1`);
  });
}
