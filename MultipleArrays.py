def MultiplyArray(longArr: list[int], shortArr: list[int]): 
    resultArr = [x*0 for x in range(len(longArr))]
    
    longArrlastIndex = len(longArr)
    carry = 0
    leftCounter = 1

    for c in shortArr[::-1]: 
        digitToMultiply = c
        longArrlastIndex = len(longArr) - leftCounter
        leftCounter += 1
        for d in longArr[::-1]:
            multiple = (d * digitToMultiply) + carry

            if longArrlastIndex < 0:
                longArrlastIndex = 0
                resultArr.insert(0,0)

            resultArr[longArrlastIndex] += multiple%10
            carry = multiple//10
            longArrlastIndex -= 1


    return resultArr

print(MultiplyArray([1,0,2,3],  [1,6]))

'''
longArr  = 123
shortArr = 16
result = [0,0,8]

shortArrlastIndex = 1
longArrlastIndex = 2


digitToMultiply = 6
carry = 1
multiple = 18
'''


