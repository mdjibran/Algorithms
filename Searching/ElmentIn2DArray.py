def FindElement(array2D, v):
    row = 0
    col = len(array2D[0])-1
    
    while row < len(array2D) and col < len(array2D[0]) and col > 0:
        val = array2D[row][col]
        if val == v:
            return True
        elif val > v:
            col = col -1
        else:
            row += 1
    
    return False


arr = [
    [-1,2,4,4,6],
    [1,5,5,9,21],
    [3,6,6,9,22],
    [3,6,8,10,24],
    [6,8,9,12,25],
    [8,10,12,13,40]    
]


print(FindElement(arr, 7))