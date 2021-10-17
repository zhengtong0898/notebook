

def lower(s: str) -> str:
    if "a" <= s <= "z": return s
    if "0" <= s <= "9": return s
    return chr(ord(s) + 32)                 # 将大写转换成小写
