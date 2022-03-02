def solution(l):
    length = len(l)
    arr = [0] * length
    i = 0
    while i < length:
        for j in range(i+1, length):
            if l[j] % l[i] == 0:
                arr[i] += 1
        i += 1

    luckySet = 0
    i = 0
    while i < length:
        for j in range(i+1, length):
            if arr[j] != 0:
                if l[j] % l[i] == 0:
                    luckySet += arr[j]
        i += 1
    return luckySet
'''


'''





arr = [1,2,3,4,5,6]
arr = [1,1,1]
print(solution(arr))


'''
(0:1,1:2) (1,3) (1,4) (1,5) (1,6)
      (2,3) (2,4) (2,5) (2,6)
            (3,4) (3,5) (3,6)
                  (4,5) (4,6)
                        (5,6)
'''