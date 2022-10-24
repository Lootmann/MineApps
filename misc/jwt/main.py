import json

from myjwt import header_encoded


def get_json(filename: str):
    with open(filename, "r") as f:
        return json.load(f)


def main():
    filename = "./jsons/header.json"
    json_file = get_json(filename)
    header = header_encoded(json_file)
    print(header)


if __name__ == "__main__":
    main()
