import sqlite3
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def Connection(db_name: str | Path):
    conn = sqlite3.connect(str(db_name))
    cursor = conn.cursor()
    yield cursor
    conn.commit()
    conn.close()


def main():
    filename = ":memory:"

    with Connection(filename) as cursor:
        cursor.execute("CREATE TABLE test (id INT, msg TEXT)")

        rows = [(1, "why"), (2, "hello"), (3, "there"), (4, ":^)")]
        cursor.executemany("INSERT INTO test VALUES (?,?)", rows)

        for row in cursor.execute("SELECT * FROM test"):
            print(row)


if __name__ == "__main__":
    main()
