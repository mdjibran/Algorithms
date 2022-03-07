def GetValidChars(s: str) -> list:
    start = ord('a')
    end = ord('z')
    lst = []
    for c in s:
        v = ord(c)
        if start <= v <= end:
            lst.append(c)
    
    return lst


def GetCharCounts(s: str) -> dict:
    d = {}

    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    
    return d


def GetOddCharCount(d: dict) -> int:
    oddCounter = 0
    for k, v in d.items():
        if v % 2 != 0:
            oddCounter += 1
    return oddCounter


def Palindrome(s: str) -> bool:
    charsToWorkWith = GetValidChars(s)
    charCounts = GetCharCounts(charsToWorkWith)
    result = GetOddCharCount(charCounts)

    return result == 1




s = 'tact coa'
print(Palindrome(s))