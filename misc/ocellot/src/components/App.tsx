import { Board } from "./Board";
import { Header } from "./Header";

import "../styles/app.css";
import React from "react";
import { CellType } from "../models/Types";
import { searchToggleCell } from "../api/Cell";

const getBoard = (): CellType[] => {
  const board = [];
  const size = 6;
  for (let i = 0; i < size * size; ++i) {
    if (i === size * 2 + 2 || i === size * 3 + 3) {
      board.push({ id: i, cell: "white" });
    } else if (i === size * 2 + 3 || i === size * 3 + 2) {
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
    if (board[idx].cell !== "") {
      console.log("this cell is already filled by piece");
      return;
    }

    // TODO: update must be immutability.
    let newBoard = [...board];
    newBoard[idx] = { id: idx, cell: turn ? "black" : "white" };

    const flipCellIdxs = searchToggleCell(idx, turn, newBoard);
    if (flipCellIdxs.length === 0) {
      console.log("There are not able to flip any cells.");
      return;
    }

    // TODO: update must be immutability.
    for (const flipIdx of flipCellIdxs) {
      newBoard[flipIdx] = { id: flipIdx, cell: turn ? "black" : "white" };
    }

    setBoard(newBoard);
    setTurn((prevTurn) => !prevTurn);
  }

  return (
    <main id="main">
      <Header turn={turn} />
      <Board board={board} putCell={putCell} />
    </main>
  );
}
