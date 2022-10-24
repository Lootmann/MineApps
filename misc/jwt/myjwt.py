import base64
import json


def header_encoded(header_json: dict) -> bytes:
    """
    header encode
    remove whitespace and newline from json,
    sorted dict key, and base64 encode with encoding=utf-9

    :param header_json: json dict
    :returns: base64 encoded json string using utf-8

    :raises keyError: this might raise error header json is not valid json.
    """
    json_string = json.dumps(header_json, separators=(",", ":"), sort_keys=True)
    return base64.b64encode(json_string.encode("utf-8"))
