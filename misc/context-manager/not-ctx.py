import sqlite3
from pathlib import Path


class Sqlite4:
    def __init__(self, filename: str | Path) -> None:
        self.db_name: str | Path = filename
        self.conn: sqlite3.Connection
        self.cursor: sqlite3.Cursor

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()


def main():
    with Sqlite4(":memory:") as cursor:
        cursor.execute(
            "CREATE TABLE test(id INTEGER PRIMARY KEY AUTOINCREMENT, msg TEXT)"
        )

        rows = [(1, "why"), (2, "hello"), (3, "there"), (4, ":^)")]
        cursor.executemany("INSERT INTO test VALUES (?,?)", rows)

        cursor.execute("SELECT * FROM test")

        for row in cursor.fetchall():
            print(row)


if __name__ == "__main__":
    main()
