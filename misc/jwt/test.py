from myjwt import claim_encoded, header_encoded


class TestEncodedHeader:
    def test_encoded_header_HS256(self):
        test_dict = {"alg": "HS256", "typ": "JWT"}

        want = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        got = header_encoded(test_dict)

        assert want == got

    def test_encoded_header_HS512(self):
        test_dict = {"alg": "HS512", "typ": "JWT"}

        want = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9"
        got = header_encoded(test_dict)

        assert want == got


class TestEncodedClaim:
    def test_encoded_claim(self):
        test_dict = {"sub": "1234567890", "name": "John Doe", "admin": True}

        want = "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9"
        got = claim_encoded(test_dict)

        assert want == got

    def test_encoded_claim_1(self):
        test_dict = {"sub": "1234567890", "iat": 1603376011}

        want = "eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNjAzMzc2MDExfQ"
        got = claim_encoded(test_dict)

        assert want == got
