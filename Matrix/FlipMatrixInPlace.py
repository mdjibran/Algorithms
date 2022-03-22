def printMat(matrix):
    for row in matrix:
        print(row)
    print("---------")


def Flip(matrix):
    source = 0
    destination = len(matrix)-1

    temp = matrix[0][2]         # 1
    matrix[0][2] = matrix[0][0] # 1 -> 3
    printMat(matrix)
    temp, matrix[2][2] = matrix[2][2], temp # 3 -> 9
    printMat(matrix)
    temp, matrix[2][0] = matrix[2][0], temp # 9 -> 7
    printMat(matrix)
    temp, matrix[0][0] = matrix[0][0], temp # 7 -> 1
    printMat(matrix)
    
    temp = matrix[1][2]         # 6
    matrix[1][2] = matrix[0][1] # 2 -> 6
    printMat(matrix)
    temp, matrix[2][1] = matrix[2][1], temp # 6 -> 8
    printMat(matrix)
    temp, matrix[1][0] = matrix[1][0], temp # 8 -> 4
    printMat(matrix)
    temp, matrix[0][1] = matrix[0][1], temp # 4 -> 2
    printMat(matrix)



Flip(
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
])









'''
[1,2,3],
[4,5,6],
[7,8,9]

[7,4,1],
[8,5,2],
[9,6,3]
'''