def Sort4Values(lst: list):
    '''
        block1 = 1
        block2 = 2
        block3 = 3
        block4 = 4
    '''


    block1 = 0
    block2 = 0
    block3 = len(lst)-2
    block4 = len(lst)-1

    while(block2 <= block4):
        if lst[block2] == 1:
            lst[block1], lst[block2] = lst[block2], lst[block1]
            block1, block2 = block1+1, block2+1

        elif lst[block2] == 2:
            block2 += 1
        
        elif lst[block2] == 3:
            lst[block3], lst[block2] = lst[block2], lst[block3]
            block3 -= 1

        else:
            lst[block4], lst[block2] = lst[block2], lst[block4]
            block4 -= 1

    
    return lst

        


print(Sort4Values([1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,3]))


