import { Board } from "./Board";
import { Header } from "./Header";

import "../styles/app.css";
import React from "react";
import { CellType } from "../models/Types";

const getBoard = (): CellType[] => {
  const board = [];
  for (let i = 0; i < 6 * 6; ++i) {
    const num = Math.random();
    if (num < 0.3) {
      board.push({ id: i, cell: "white" });
    } else if (num < 0.6) {
      board.push({ id: i, cell: "black" });
    } else {
      board.push({ id: i, cell: "" });
    }
  }
  return board;
};

export function App() {
  const [board, setBoard] = React.useState(getBoard());
  const [turn, setTurn] = React.useState<boolean>(true);

  function putCell(idx: number) {
    let newBoard = [...board];
    newBoard[idx] = { id: idx, cell: turn ? "black" : "white" };

    setBoard(newBoard);
    setTurn((prevTurn) => !prevTurn);
  }

  return (
    <main id="main">
      <Header />
      <Board board={board} putCell={putCell} />
    </main>
  );
}
