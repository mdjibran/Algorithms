def binary(arr, key):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    return -1



print(binary([3,6,9,12,45,53], 53))
