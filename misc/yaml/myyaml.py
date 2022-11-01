"""
<empty> := ""
<char>  := a-zA-Z
<int>   := 0-9
<elem>  := <char> | <int> | <empty>
"""


def check_type(line: str) -> str:
    """
    when line is dict, line should have '<char> :'
    when line is array, line should have '- <elem>'
    """

    # NOTE: dict can nest
    if ":" in line:
        s = line.split(":")
        if len(s) == 2:
            return "dict"

    if line[0] == "-":
        return "array"

    raise ValueError("Invalid Yaml")


def convert_value(elem: str) -> str | int:
    try:
        return int(elem)
    except:
        return elem.strip()


def load(text: str) -> dict | list | None:
    if text == "":
        return None

    d = dict()

    for _, line in enumerate(text.rstrip().split("\n")):
        token_type = check_type(line)

        if token_type == "dict":
            left, right = line.split(":")
            d[left] = convert_value(right)

        if token_type == "array":
            pass

    return d
