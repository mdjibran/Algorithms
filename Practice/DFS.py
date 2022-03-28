def isValid(newRow, newCol, rowSize, colSize, isVisited):
    if newRow >= 0 and newCol >= 0 and \
            newRow < rowSize and newCol < colSize and \
            isVisited[newRow][newCol] == False:

        isVisited[newRow][newCol] = True
        return True
    
    return False


def FindPath(matrix, dst):
    q = []
    r, c, distance = 0, 0, 0
    q.append((r, c, distance))
    rowSize = len(matrix)
    colSize = len(matrix[0])
    isVisited = [[False for x in range(colSize)] for x in range(rowSize)]
    isVisited[r][c] = True

    while q:
        #print(q)
        row, col, d = q.pop(0)
        if matrix[row][col] == dst:
            return d
        new_dst = d +1
        if isValid(row+1, col, rowSize, colSize, isVisited):
            q.append((row+1, col, new_dst))
        if isValid(row-1, col, rowSize, colSize, isVisited):
            q.append((row-1, col, new_dst))
        if isValid(row, col+1, rowSize, colSize, isVisited):
            q.append((row, col+1, new_dst))
        if isValid(row, col-1, rowSize, colSize, isVisited):
            q.append((row, col-1, new_dst))
        
    c = 55
    return -1


m = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 9, 1],
    [0, 0, 1, 1]
]

print(FindPath(m, 9))