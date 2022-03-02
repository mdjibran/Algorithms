def solution(l, t):

    slow, fast = 0, 0
    pastValue = 0

    while slow < len(l):
        while fast < len(l) and pastValue < t:
            pastValue += l[fast]
            fast += 1
       
        if pastValue == t:
            return [slow, fast-1]
        slow+= 1
        fast = slow
        pastValue = 0
    return [-1, -1]


arr = [4, 3, 10, 2, 8]
#t = 12
#arr = [4, 3, 5, 7, 8]

arr = [10, 4, 6, 1, 10, 10, 10, 10, 10, 10, 10, 7]
#arr = [1,2,3,4]
t = 57
print(solution(arr, t))