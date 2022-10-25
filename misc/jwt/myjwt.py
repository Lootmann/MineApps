import base64
import hashlib
import hmac
import json
from typing import Callable


def to_base64(json_dict: dict) -> bytes:
    data_bytes = json.dumps(json_dict, separators=(",", ":")).encode("utf-8")
    encoded = base64.urlsafe_b64encode(data_bytes).strip(b"=")
    return encoded


def get_algorithm(header_json: dict) -> Callable:
    if "alg" not in header_json:
        raise ValueError("Header has NO alg")

    algorithm = header_json["alg"]

    if algorithm == "HS256":
        return hashlib.sha256

    if algorithm == "HS512":
        return hashlib.sha512

    raise ValueError("Wrong algorithm")


def to_signature(b64_header: bytes, b64_claim: bytes, secret_key: str, algorithm: Callable) -> str:
    payload = b64_header + b"." + b64_claim
    byte_secret = bytes(secret_key, "utf-8")

    signature_bytes = base64.urlsafe_b64encode(
        hmac.new(byte_secret, payload, algorithm).digest(),
    )

    return signature_bytes.decode("utf-8").rstrip("=")


def jwt(header: dict, claim: dict, secret_key: str) -> str:
    b64_header = to_base64(header)
    b64_claim = to_base64(claim)
    algorithm = get_algorithm(header)
    signature = to_signature(b64_header, b64_claim, secret_key, algorithm=algorithm)

    jwt = b64_header.decode() + "." + b64_claim.decode() + "." + signature
    return jwt
