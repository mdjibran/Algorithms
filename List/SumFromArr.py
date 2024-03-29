'''
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


def twoSum(arr, target):
    comps = {}

    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in comps.keys():
            return [i, comps[compliment]]
        else:
            comps[arr[i]] = i
    
    return []



arr = [2,7,11,15]
print(twoSum(arr, 9))
