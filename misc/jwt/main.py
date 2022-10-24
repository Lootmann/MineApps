import json

from myjwt import claim_encoded, header_encoded, jwt


def get_json(filename: str):
    with open(filename, "r") as f:
        return json.load(f)


def main():
    header_json = get_json("./jsons/header.json")
    claim_json = get_json("./jsons/claim.json")

    signature = jwt(header_json, claim_json, "abcde")
    print(signature)


if __name__ == "__main__":
    main()
