from collections import deque

def is_valid(row, col, numRows, numCols, matrix, visited):
    if row >= 0 and col >= 0 and \
        row < numRows and col < numCols and \
        matrix[row][col] in (1, 9) and \
        visited[row][col] == False:
        return True
    else:
        return False

def getPath(matrix, numRows, numCols):
    queue = deque()
    row, col = 0, 0
    queue.append((row, col, 0))

    visited = [[False for _ in range(numCols)] for _ in range(numRows)]
    distance_matrix = [[-1 for _ in range(numCols)] for _ in range(numRows)]

    visited[row][col] = True

    while queue:
        row, col, distance = queue.popleft()
        distance_matrix[row][col] = distance

        if matrix[row][col] == 9:
            return distance
        new_distance = distance + 1

        if is_valid(row+1, col, numRows, numCols, matrix, visited):
            queue.append((row+1, col, new_distance))

        if is_valid(row-1, col, numRows, numCols, matrix, visited):
            queue.append((row-1, col, new_distance))

        if is_valid(row, col+1, numRows, numCols, matrix, visited):
            queue.append((row, col+1, new_distance))

        if is_valid(row, col-1, numRows, numCols, matrix, visited):
            queue.append((row, col-1, new_distance))


    return -1




if __name__ == '__main__':
    numRows = 5
    numCols = 4
    matrix = [
        [1, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 9, 1],
        [0, 0, 1, 1]
    ]

    #print(getPath(matrix, numRows, numCols))


    numRows = 3
    numCols = 3
    matrix = [
        [1, 0, 0],
        [1, 0, 0],
        [1, 9, 1]
    ]

    print(getPath(matrix, numRows, numCols))
