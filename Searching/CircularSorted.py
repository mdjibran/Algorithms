import sys



def MinValue(lst: list):
    low = 0
    high = len(lst) -1

    while low < high:
        mid = low + (high-low)//2

        if lst[mid] > lst[high]:
            low = mid + 1
        elif lst[mid] < lst[high]:
            high = mid
    
    return lst[high]






print(MinValue([378,478,550,631,103,203,220,234,279,368]))
print(MinValue([631,103,203,220,234,279,368,433,564]))