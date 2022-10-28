import { Outlet, Link } from "react-router-dom";

export function App() {
  return (
    <>
      <header id="header">
        <ul>
          <li>
            <Link to={"/test"}>Test</Link>
          </li>

          <li>
            <Link to={"/hoge"}>Hoge</Link>
          </li>
        </ul>
      </header>

      <main id="main">
        <Outlet />
      </main>
    </>
  );
}
