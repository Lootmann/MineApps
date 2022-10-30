export type CellType = {
  id: number;
  cell: string;
};

export type BoardProps = {
  board: CellType[];
  putCell: (cellId: number) => void;
};

export type HeaderProps = {
  turn: boolean;
};
