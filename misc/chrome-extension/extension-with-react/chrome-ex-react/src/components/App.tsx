import { Sidebar } from "./Sidebar";
import { TodoList } from "./Todo";

export function App() {
  return (
    <div id="wrapper">
      <Sidebar />
      <TodoList />
    </div>
  );
}
