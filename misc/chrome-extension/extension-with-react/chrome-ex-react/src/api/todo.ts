/**
 * todo.ts
 *
 * when save to google chrome.storage,
 * convert array(Todo[]) to JSON
 *
 * when load from google chorme.storage,
 * convert JSON to array(Todo[])
 */

export function getTodo() {
  chrome.storage.sync.get(["todo"], function (todo) {
    console.log(todo);
  });
}

export function updateTodo(id: number) {
  const json = JSON.stringify({ hello: "world" });
  chrome.storage.sync.set({ todos: json }, function () {
    console.log(`value is set to 1`);
  });
}
