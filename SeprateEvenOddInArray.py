def SeprateArray(arr):

    evenPos = 0
    oddPos = len(arr) -1

    while(evenPos < oddPos and oddPos < len(arr)):
        if(arr[evenPos] % 2 == 0):
            evenPos += 1
        else:
            arr[evenPos], arr[oddPos] = arr[oddPos], arr[evenPos]
            oddPos -= 1

    return arr
        


print(SeprateArray([11,19,21,17,9,5,4,13,2,8,20]))

