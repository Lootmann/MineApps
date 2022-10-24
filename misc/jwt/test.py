from myjwt import header_encoded


class TestEncodedHeader:
    def test_encoded_header_HS256(self):
        test_dict = {"alg": "HS256", "typ": "JWT"}

        want = b"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        got = header_encoded(test_dict)

        assert want == got

    def test_encoded_header_HS512(self):
        test_dict = {"alg": "HS512", "typ": "JWT"}

        want = b"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9"
        got = header_encoded(test_dict)

        assert want == got
