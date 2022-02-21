from subprocess import HIGH_PRIORITY_CLASS


def GetFirstIdx(lst: list, key:int):
    low = 0
    high = len(lst)-1
    result = -1

    while low <= high:
        mid = low + (high-low)//2
        v = lst[mid]
        if v == key:
            result = mid
            high = mid - 1
        elif v > key:
            high = mid-1
        else:            
            low = mid+1
        
    return result





print(GetFirstIdx([1,2,3,4,5,6,8,8,9,10], 8))