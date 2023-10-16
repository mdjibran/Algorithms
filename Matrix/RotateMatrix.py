'''
first
| 5  | 1  | 9  | 11 |          
| 2  | 4  | 8  | 10 |
| 13 | 3  | 6  | 7  |
| 15 | 14 | 12 | 16 |

final
| 15  | 13 | 2  | 5  |
| 14  | 3  | 4  | 1  |
| 12  | 6  | 8  | 9  |
| 16  | 7  | 10 | 11 |

[
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13,3, 6, 7],
    [15, 14,12, 16]
]

[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
first
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

final
| 7 | 4 | 1 |
| 8 | 5 | 2 |
| 9 | 6 | 3 |

'''

def displayMat(mat, line, temp):
    print("\n\n"+line+":")
    for row in mat:
        print(row)
    print("Temp: "+ str(temp))

def rotateMatrixInPlace(mat):

    left, right = 0, len(mat)-1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = mat[top][left+i]

            mat[top][left+i] = mat[bottom-i][left]
            mat[bottom-i][left] = mat[bottom][right-i]
            mat[bottom][right-i] = mat[top+i][right]
            mat[top+i][right]= topLeft
        right -= 1
        left += 1
    displayMat(mat, "", topLeft)


    
def rotateMatrixAdditionalMAtrix(matrix):
    size = len(matrix)
    temp = [ [0 for x in range(size)] for y in range(size)]
    col = size

    for row in matrix:        
        col, tempMatrixRow = col-1, 0

        for i in range(0, size):
            temp[tempMatrixRow][col] = row[i]   
            tempMatrixRow += 1           
    displayMat(temp, "", 0)
    return temp




mat = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13,3, 6, 7],
    [15, 14,12, 16]
]

#rotateMatrixInPlace(mat)
rotateMatrixAdditionalMAtrix(mat)

    

