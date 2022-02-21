import sys

def MinMax(arr):
    slow, fast = 0, 1
    maxVal = -sys.maxsize
    minVal = sys.maxsize

    while fast < len(arr):
        minVal = min(minVal)

    return (minVal, maxVal)



print(MinMax([3,2,5,1,6,1]))