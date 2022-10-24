import React from "react";
import { Link } from "../components/Link";
import { LinkType } from "../models/Link";

export function App() {
  const [links, setLinks] = React.useState<LinkType[]>([]);
  const linkRef = React.useRef<HTMLInputElement>(null);
  const [error, setError] = React.useState<string>("");

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (linkRef.current === null) {
      return;
    }

    const link = linkRef.current?.value;

    if (link === undefined || link === null) {
      setError("NEED LINK");
      return;
    }

    if (link.length < 5) {
      setError("link should be more than 5 length");
      return;
    }

    setError("");
    setLinks((prevLinks) => {
      return [...prevLinks, new LinkType(link)];
    });

    // clear url
    linkRef.current.value = "";
  }

  const renderLink = links.map((l) => {
    return (
      <li key={l.shorten_link} className="link">
        <Link link={l.link} shorten_link={l.shorten_link} />
      </li>
    );
  });

  return (
    <main id="main">
      <h1>hello world</h1>

      {error !== "" && <p className="error">{error}</p>}

      <form
        action=""
        method="get"
        className="form"
        onSubmit={(e) => handleSubmit(e)}
      >
        <button type="submit">Create</button>
        <input type="text" name="link" id="link" ref={linkRef} autoFocus />
      </form>

      <div className="link-list">
        <ul>{links.length !== 0 ? renderLink : <li>no links</li>}</ul>
      </div>
    </main>
  );
}
