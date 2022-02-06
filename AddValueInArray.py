def addInArray(lst: list, value_to_add: int):
    
    lastIndex = len(lst) - 1

    while value_to_add:    
        if lastIndex < 0:
            lst.insert(0, 0)
            lastIndex = 0

        lastValue = lst[lastIndex]  
        value_to_add = lastValue + value_to_add  
        lst[lastIndex] = value_to_add%10
        lastIndex-=1
        value_to_add = value_to_add // 10
        


    return lst



print(addInArray([9,8,2,9], 1))
