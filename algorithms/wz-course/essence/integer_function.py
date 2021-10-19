

def str_to_int(s: str) -> int:
    sign = s[0] if s[0] in ("-", "+") else ""
    new_s = s[1:] if sign else s
    kv = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    if not new_s[0].isdigit():
        raise ValueError(f"invalid literal for int() with base 10: '{new_s}'")

    result = 0
    for i in range(len(new_s)):
        char = new_s[i]
        result = (result * 10) + kv[char]

    if sign == "-":
        result *= -1

    return result


if __name__ == '__main__':
    print(str_to_int("-1234"))
