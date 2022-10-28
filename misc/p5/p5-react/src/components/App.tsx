import { Outlet, Link } from "react-router-dom";

export function App() {
  return (
    <>
      <header id="header">
        <ul>
          <li>
            <Link to={"/about"}>About</Link>
          </li>
          <li>b</li>
          <li>c</li>
        </ul>
      </header>

      <main id="main">
        <Outlet />
      </main>
    </>
  );
}
