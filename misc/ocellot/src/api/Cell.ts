import { CellType } from "../models/Types";

/**
 *
 * @param idx {number}
 * @param turn {boolean}
 * @param board {CellType[]}
 * @returns flip cell idxs {number[]}
 */
export const searchToggleCell = (
  idx: number,
  turn: boolean,
  board: CellType[]
): number[] => {
  const size = 6;
  const mineCell = turn ? "black" : "white";
  const enemyCell = !turn ? "black" : "white";

  // TODO: vertical
  // impl current to top search
  // impl current to bottom search

  // horizontal
  // search flippable cell from current to left position.
  const toLeftIdxs = currentToLeft(idx, size, mineCell, enemyCell, board);
  const toRightIdxs = currentToRight(idx, size, mineCell, enemyCell, board);

  // TODO: horizontal
  // impl current to top-right
  // impl current to bottom-left
  // impl current to top-left
  // impl current to bottom-right

  return [...toLeftIdxs, ...toRightIdxs];
};

function currentToLeft(
  currenIdx: number,
  boardSize: number,
  mineCell: string,
  enemyCell: string,
  board: CellType[]
): number[] {
  const col_min = Math.floor(currenIdx / boardSize) * boardSize;

  let is_ok: boolean = true;
  const result = [];

  for (let i = currenIdx - 1; i >= col_min; --i) {
    if (
      i === currenIdx - 1 &&
      (board[i].cell === "" || board[i].cell === mineCell)
    ) {
      is_ok = false;
      break;
    }

    if (board[i].cell === "") {
      is_ok = false;
      break;
    }

    if (board[i].cell === enemyCell) {
      is_ok = true;
      result.push(i);
    }

    if (board[i].cell === mineCell) {
      is_ok = true;
      break;
    }
  }

  if (is_ok) return result;
  else return [];
}

function currentToRight(
  currenIdx: number,
  boardSize: number,
  mineCell: string,
  enemyCell: string,
  board: CellType[]
): number[] {
  const col_max = Math.floor(currenIdx / boardSize + 1) * boardSize;

  let is_ok: boolean = true;
  const result = [];

  for (let i = currenIdx + 1; i <= col_max; ++i) {
    if (
      i === currenIdx + 1 &&
      (board[i].cell === "" || board[i].cell === mineCell)
    ) {
      is_ok = false;
      break;
    }

    if (board[i].cell === "") {
      is_ok = false;
      break;
    }

    if (board[i].cell === enemyCell) {
      is_ok = true;
      result.push(i);
      continue;
    }

    if (board[i].cell === mineCell) {
      is_ok = true;
      break;
    }
  }

  if (is_ok) return result;
  else return [];
}
