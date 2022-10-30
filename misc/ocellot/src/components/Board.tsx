import "../styles/board.css";
import { BoardProps } from "../models/Types";

export function Board(props: BoardProps) {
  return (
    <div id="board">
      {props.board.map((cell) => {
        return (
          <span
            className="cell"
            key={cell.id}
            onClick={() => props.putCell(cell.id)}
          >
            {cell.cell === "" ? (
              <span></span>
            ) : cell.cell === "black" ? (
              <span className="black"></span>
            ) : (
              <span className="white"></span>
            )}
          </span>
        );
      })}
    </div>
  );
}
