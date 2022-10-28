import React from "react";

export function App() {
  // chrome storage
  chrome.storage.sync.set({ id: 1 }, function () {
    console.log(`value is set to 1`);
  });

  chrome.storage.sync.get(["id"], function (result) {
    console.log("result = ", result.id);
  });

  return (
    <main id="main">
      <h1>hello world</h1>

      <p>Huge :^)</p>
    </main>
  );
}
