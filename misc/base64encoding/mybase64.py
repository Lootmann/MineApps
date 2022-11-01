from string import ascii_lowercase, ascii_uppercase, digits


class Base64:
    @classmethod
    def bit2char(cls, bit: str) -> str:
        # value type validation
        idx = int(bit, 2)

        # range validation
        if not 0 <= idx <= 63:
            raise ValueError("outbound idx")

        if 0 <= idx <= 25:
            return ascii_uppercase[idx]
        elif 26 <= idx <= 51:
            return ascii_lowercase[idx - 26]
        elif 52 <= idx <= 61:
            return digits[idx - 52]
        elif idx == 62:
            return "+"
        else:
            return "-"

    @classmethod
    def char2bit(cls, char: str) -> str:
        """
        'A': 000000 ~ 'Z': 011001
        'a': 011010 ~ 'z': 110011
        '0': 110100 ~ '9': 111101
        '+': 111110
        '-': 111111
        """
        if len(char) != 1:
            raise ValueError("variable 'char' must be one char.")

        if "A" <= char <= "Z":
            idx = ord(char) - ord("A")
            return "{:0>6s}".format(bin(idx)[2:])

        if "a" <= char <= "z":
            base_idx = int("011010", 2)
            idx = base_idx + ord(char) - ord("a")
            return "{:0>6s}".format(bin(idx)[2:])

        if "0" <= char <= "9":
            base_idx = int("110100", 2)
            idx = base_idx + int(char)
            return "{:0>6s}".format(bin(idx)[2:])

        if char == "+":
            return "111110"

        if char == "-":
            return "111111"

        raise ValueError("This char: {} is NOT in base64encode map".format(char))

    @classmethod
    def convert_bit_series(cls, string: str) -> list:
        # convet string to str bit
        bits = []
        for c in string:
            bits.append("{:0>8s}".format(bin(ord(c))[2:]))

        # and divides the bits string into 6-bit segments
        concat = "".join(bits)

        if len(concat) % 6 != 0:
            concat += "0" * (6 - len(concat) % 6)

        return [concat[6 * i : 6 * i + 6] for i in range(len(concat) // 6)]

    @classmethod
    def convert_bit_to_base64encode(cls, splitted_bit: list) -> str:
        # convert bit to encoding char with base64 mapping
        encode_string = "".join([Base64.bit2char(bit) for bit in splitted_bit])

        # padding
        if len(encode_string) % 4 != 0:
            encode_string += "=" * (4 - len(encode_string) % 4)

        return encode_string

    @classmethod
    def base64encoding(cls, src: str) -> str:
        # string to bit
        bit_series = cls.convert_bit_series(src)

        # bit to base64encoding
        encode_string = cls.convert_bit_to_base64encode(bit_series)

        return encode_string

    @classmethod
    def base64decoding(cls, src: str) -> str:
        # strip '=' by last bit
        stripped = src.rstrip("=")

        # convert to base64 bit
        base64_chars = [cls.char2bit(char) for char in list(stripped)]

        # concat 8-bit segments
        concat = "".join(base64_chars)

        splitted = [concat[8 * i : 8 * i + 8] for i in range(len(concat) // 8)]

        # bit to char
        return "".join(chr(int(bits, 2)) for bits in splitted)
