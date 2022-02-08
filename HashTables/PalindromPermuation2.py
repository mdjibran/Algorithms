'''
Palindrom string

'''
from collections import defaultdict

def SetDict(s: str):
    dict = defaultdict(str)
    for c in s:
        if c not in dict:
            dict[c] =  1
        else:
            dict[c] += 1
    return dict

def CheckPalindrom(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
        
    d1 = SetDict(str1)
    for c in str2:
        if c not in d1:
            return False
        else:
            d1[c] -= 1
    
        if d1[c] == 0:
            d1.pop(c, 'None')

    return d1 == {}


print(CheckPalindrom("edified", "deified"))