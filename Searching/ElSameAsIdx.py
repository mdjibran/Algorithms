def CheckIfSame(lst: list):
    low = 0
    high = len(lst) -1

    while low <= high:
        mid = low + (high - low)//2

        if lst[mid] == mid:
            return mid
        elif lst[mid] > mid:
            high = mid - 1
        else:
            low = mid +1
        
    return -1


print(CheckIfSame([2,3,4,5,6,7,8]))