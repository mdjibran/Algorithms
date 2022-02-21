def FindSquare(v: int):
    low = 0
    high = v

    while low < high:
        mid = low + (high-low)//2

        sq = mid*mid
        
        if sq > v:
            high = mid -1
        else:
            low = mid + 1
    
    return low-1

        




print(FindSquare(300))