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
            dict[c] = dict[c] + 1
    return dict


def CheckPalindrom(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
        
    d1 = SetDict(str1)
    d2 = SetDict(str2)

    for k, v in d1.items():
        if k not in d2 or d2[k] != v:
            return False
    
    return True


    
    


print(CheckPalindrom("edified", "deified"))