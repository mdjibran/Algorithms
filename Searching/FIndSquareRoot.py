
def FindSqRoot(x: int):
    low, high = (0, x) if x > 0 else (x,0)

    while low <= high:
        mid = low + (high - low)//2

        sq = mid*mid

        if sq > x:
            high = mid -1
        else:
            low = mid + 1
        
    return low-1
        




print(FindSqRoot(49))