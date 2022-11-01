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
        elif 26 <= idx <= 52:
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
    def base64encoding(cls, src: str) -> str:
        return ""

    @classmethod
    def base64decoding(cls, src: str) -> str:
        return ""


"""
000000	A
000001	B
000010	C
000011	D
000100	E
000101	F
000110	G
000111	H
001000	I
001001	J
001010	K
001011	L
001100	M
001101	N
001110	O
001111	P
010000	Q
010001	R
010010	S
010011	T
010100	U
010101	V
010110	W
010111	X
011000	Y
011001	Z
011010	a
011011	b
011100	c
011101	d
011110	e
011111	f
ビット列	Base64文字
100000	g
100001	h
100010	i
100011	j
100100	k
100101	l
100110	m
100111	n
101000	o
101001	p
101010	q
101011	r
101100	s
101101	t
101110	u
101111	v
110000	w
110001	x
110010	y
110011	z
110100	0
110101	1
110110	2
110111	3
111000	4
111001	5
111010	6
111011	7
111100	8
111101	9
111110	+
111111	/
"""
