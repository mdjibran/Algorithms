def SortColors(nums):


    zeros = 0
    ones = 0
    twos = len(nums)-1
        
    while ones <= twos:
        if nums[ones] == 1:                          
            ones += 1
        elif nums[ones] ==  0:            
            nums[zeros], nums[ones] = nums[ones], nums[zeros]  
            zeros, ones = zeros + 1, ones +1
        else:                
            nums[ones], nums[twos] = nums[twos], nums[ones]
            twos -= 1
                
    return nums



print(SortColors([1,2]))


'''
input  =  2,0,1
I1     =  1,0,2
I2     =  1,0,2
I3     =    


zeros = 0
ones = 1
twos = 1



'''