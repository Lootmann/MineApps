def bin2decimal(binary: str) -> int:
    decimal = 0

    for ch in binary:
        decimal = decimal * 2
        if ch == "1":
            decimal += 1

    return decimal


def validate(binary: str) -> None:
    for ch in binary:
        if ch not in ("0", "1"):
            raise ValueError("You can only input 0 or 1 digit")


def main():
    binary = input("input binary digit: ")

    try:
        validate(binary)
    except ValueError as e:
        print(e)

    print(bin2decimal(binary))


if __name__ == "__main__":
    main()
