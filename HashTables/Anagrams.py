'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/valid-anagram/
'''
def SetDict(s):
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d 
            
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    
    d = self.SetDict(s)
    d2 = self.SetDict(t)
    
    for k, v in d.items():
        if k not in d2 or d[k] != d2[k]:
            return False
        
    return True