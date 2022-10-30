import "../styles/header.css";
import { HeaderProps } from "../models/Types";

export function Header(props: HeaderProps) {
  return (
    <header id="header">
      <h1 className="h1">Header</h1>
      <p className="turn">Turn : {props.turn ? "White" : "Black"}</p>
    </header>
  );
}
