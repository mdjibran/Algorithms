'''
USING DEFAULT DICT
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/group-anagrams/


'''


from collections import defaultdict
import string

def GroupAnagrams(strs: list[str]):
    dict = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s.lower()))
        dict[key].append(s)
    
    result = []
    for k,v in dict.items():
            result.append(dict[k])
    
    return result



#print(GroupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
print(GroupAnagrams(["debitcard","elvis","silent","badcredit","lives","freedom","listen","levis","money"]))






