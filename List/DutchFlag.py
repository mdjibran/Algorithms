def SortLst(pivot_index: int, lst:  list):
    less = 0
    equal = 0
    high = len(lst) - 1
    pivot = lst[pivot_index]

    while(equal <= high):
        if lst[equal] < pivot:
            lst[less], lst[equal]= lst[equal], lst[less]
            less, equal = less + 1, equal + 1

        elif lst[equal] == pivot:
            equal += 1
        
        else:
            lst[high], lst[equal] = lst[equal], lst[high]
            high -= 1

    return lst








#print(SortLst(5, [11,19,21,17,9,5,4,13,2,8,20]))
#print(SortLst(2, [0,1,2,0,2,1,1]))
print(SortLst(4, [0,6,11,14,6,2,-1,62]))

'''


[6,5,4]
   ^

'''

