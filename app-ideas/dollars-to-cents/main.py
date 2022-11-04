from collections import OrderedDict


def get_user_input() -> float:
    user_input = input("Input Dollar : $")

    try:
        cents = float(user_input)
    except:
        raise ValueError("input should be float number")

    # cents are 0.X, 0.XX
    # 0.XXX is wrong
    if cents * 1000 % 10 != 0:
        raise ValueError("")

    return cents


def convert_dollar_to_cent(dollar: float) -> dict:

    # e.x.) 0.58 * 100 = 57.99999999...
    # so, this needs round float
    dollar = int(round(dollar * 100, 2))

    cent_dict = OrderedDict(quarter=25, dim=10, nickel=5, penny=1)
    res = {}

    # greedy
    for cent_name, value in cent_dict.items():
        div, mod = divmod(dollar, value)
        res[cent_name] = div
        dollar = mod

    return res


def main():
    inputs = get_user_input()

    res = convert_dollar_to_cent(inputs)
    print(res)


if __name__ == "__main__":
    main()
