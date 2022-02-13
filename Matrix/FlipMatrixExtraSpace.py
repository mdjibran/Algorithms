def FlipMatrix(matrix):
    size = len(matrix)
    temp = [ [0 for x in range(3)] for y in range(3)]
    col = size

    for row in matrix:        
        col, tRow = col-1, 0

        for i in range(0, size):
            temp[tRow][col] = row[i]   
            tRow += 1           
    
    return temp





print(FlipMatrix([[1,2,3],[4,5,6],[7,8,9]]))



