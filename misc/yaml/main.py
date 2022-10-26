from pathlib import Path

import myyaml
import yaml


def get_files(dirname: str) -> list:
    return [str(p.expanduser()) for p in Path(dirname).glob("*.yaml")]


def main():
    paths = get_files("yamls")

    for path in paths:
        print(">>>", path)
        with open(path, "r") as f:
            print(yaml.safe_load(f))
        print()

    for path in paths:
        print(f">>> {path}")

        with open(path, "r") as f:
            print(myyaml.load(f.read()))
        print()


if __name__ == "__main__":
    main()
