def CheckDuplicate(s: str):
    s = ''.join(sorted(s))
    char1 = 0
    char2 = char1 + 1

    while char2 < len(s):
        if s[char1] == s[char2]:
            return False
        char1, char2 = char1 + 1, char2 + 1
    return True
    
    






print(CheckDuplicate('abc'))