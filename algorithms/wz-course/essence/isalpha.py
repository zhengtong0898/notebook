

def isalpha(s: str) -> bool:
    if "a" <= s <= "z": return True
    if "A" <= s <= "Z": return True
    if "0" <= s <= "9": return True
    return False
