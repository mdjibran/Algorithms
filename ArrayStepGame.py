def CheckGame(nums: list[int]):
    lastIndex = len(nums) - 1
    i = 0
    distance = 0
        
    while i <= distance and distance < lastIndex:
        distance = max(distance, i+nums[i])
        i+=1
        
    return distance >= lastIndex




print(CheckGame([3,3,1,0,2,0,1]))



