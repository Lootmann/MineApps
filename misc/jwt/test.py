import hashlib

import pytest

from myjwt import get_algorithm, jwt, to_base64, to_signature


class TestEncodedHeader:
    def test_encoded_header_HS256(self):
        test_dict = {"alg": "HS256", "typ": "JWT"}

        want = b"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        got = to_base64(test_dict)

        assert want == got

    def test_encoded_header_HS512(self):
        test_dict = {"alg": "HS512", "typ": "JWT"}

        want = b"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9"
        got = to_base64(test_dict)

        assert want == got


class TestEncodedClaim:
    def test_encoded_claim(self):
        test_dict = {"sub": "1234567890", "name": "John Doe", "admin": True}

        want = b"eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9"
        got = to_base64(test_dict)

        assert want == got

    def test_encoded_claim_1(self):
        test_dict = {"sub": "1234567890", "iat": 1603376011}

        want = b"eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNjAzMzc2MDExfQ"
        got = to_base64(test_dict)

        assert want == got


class TestGetAlgorithm:
    def test_header_has_HS256(self):
        header = {"alg": "HS256", "typ": "JWT"}

        got = get_algorithm(header)
        want = hashlib.sha256

        assert got == want

    def test_header_has_HS512(self):
        header = {"alg": "HS512", "typ": "JWT"}

        got = get_algorithm(header)
        want = hashlib.sha512

        assert got == want

    def test_header_has_weird_algorithm(self):
        header = {"alg": "PES12", "typ": "JWT"}

        with pytest.raises(ValueError):
            get_algorithm(header)

    def test_header_has_no_alg_field(self):
        header = {"gori": "HS256", "typ": "JWT"}

        with pytest.raises(ValueError):
            get_algorithm(header)


class TestSigunature:
    def test_signature_HS256(self):
        header = {"alg": "HS256", "typ": "JWT"}
        claim = {"sub": "1234567890", "iat": 1516239022, "exp": 1500123345}
        secret_key = "secret-key-ever"

        got = to_signature(to_base64(header), to_base64(claim), secret_key, get_algorithm(header))
        want = "ipMVS2ucniIu6xuTkAOq8OpXtQ0yfOO5AVL0dxOeWgU"

        assert got == want

    def test_signature_HS512(self):
        header = {"alg": "HS512", "typ": "JWT"}
        claim = {"sub": "1234567890", "iat": 1516239022, "exp": 1500123345}
        secret_key = "secret-key-ever"

        got = to_signature(to_base64(header), to_base64(claim), secret_key, get_algorithm(header))
        want = "Tpy4hAQ6lcWP8o_GjTdqA1oflyWhEUDbak6wRKtG4GWsdU480y56hSKvIrXPUcjeiPXj0M0PuARuEBRb00YVVg"

        assert got == want


class TestCreateJWT:
    def test_jwt(self):
        header = {"alg": "HS256", "typ": "JWT"}
        claim = {
            "iat": 1653199095,
            "jti": "da5dd8a6-15c5-4197-9f6b-cc0f6051dcf2",
            "type": "access",
            "sub": "U0000000120",
            "nbf": 1653199095,
            "exp": 1653199995,
        }
        secret_key = "SecretKey"

        got = jwt(header, claim, secret_key)
        want = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTMxOTkwOTUsImp0aSI6ImRhNWRkOGE2LTE1YzUtNDE5Ny05ZjZiLWNjMGY2MDUxZGNmMiIsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiJVMDAwMDAwMDEyMCIsIm5iZiI6MTY1MzE5OTA5NSwiZXhwIjoxNjUzMTk5OTk1fQ.TginLybmda6C4UA7qp_os-AAcIvxSAFd2wM2bOkU4m4"

        assert want == got

    def test_jwt_1(self):

        header = {"alg": "HS512", "typ": "JWT"}
        claim = {
            "iss": "idg",
            "sub": "1234567890",
            "aud": "urn:myEntity",
            "name": "John Doe",
            "admin": True,
            "exp": "1544196045",
        }
        secret_key = "hogehoge-secret"

        got = jwt(header, claim, secret_key)
        want = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJpZGciLCJzdWIiOiIxMjM0NTY3ODkwIiwiYXVkIjoidXJuOm15RW50aXR5IiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImV4cCI6IjE1NDQxOTYwNDUifQ.TGSK4gfV8rtefdksChdQwUQSiCTRP1NRZruRsBngjGVHJ5LBwxtxkHgKJR1y7rm7aKhUN06PruCAVwCN9P5PJg"

        assert got == want
