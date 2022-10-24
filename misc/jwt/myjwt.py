import base64
import hashlib
import hmac
import json


def header_encoded(header_json: dict) -> str:
    """
    header encode
    remove whitespace and newline from json,
    sorted dict key, and base64 encode with encoding=utf-9

    :param header_json: json dict
    :returns: base64 encoded string using utf-8

    :raises keyError: this might raise error header json is not valid json.
    """
    json_string = json.dumps(header_json, separators=(",", ":"), sort_keys=True)
    return base64.b64encode(json_string.encode("utf-8")).decode("utf-8")


def claim_encoded(claim_json: dict) -> str:
    """
    claim encoded

    same as header_encoded
    claim do not need key sorted.

    :param claim_json: json dict
    :returns: base64 encoded string using utf-8
    """
    json_string = json.dumps(claim_json, separators=(",", ":"))
    return base64.b64encode(json_string.encode("utf-8")).decode("utf-8").strip("=")


def jwt(header_json: dict, claim_json: dict, secret_key: str) -> str:
    """
    FIXME: not working correctly :^)
    """
    header = header_encoded(header_json)
    claim = claim_encoded(claim_json)

    signature = hmac.new(
        bytes(secret_key, "utf-8"),
        bytes(header + "." + claim, "utf-8"),
        hashlib.sha256,
    ).hexdigest()

    return base64.b64encode(signature.encode("utf-8")).decode("utf-8")
