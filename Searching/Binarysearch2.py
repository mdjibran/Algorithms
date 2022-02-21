from turtle import left, right


def Search(lst: list[int], key: int):
    
    low = 0
    high = len(lst)-1
    

    while  low <= high:
        mid = (low + high)//2
        val = lst[mid]

        if key > val:
            low = mid
        elif key < val:
            high = mid
        
        else:
            return mid

    return -1





print(Search([1,2,3,4,5,6,7,8,9], 8))