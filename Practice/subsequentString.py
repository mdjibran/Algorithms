def SplitSimilar(arr: str) -> str:
    sArr = sorted(arr)
    output = sArr[0]
    left, right = 1, len(s) - 1
    
    while left <= right:
        if sArr[left] == output[len(output) - 1]:
            output += sArr[right]
            right -= 1
        else:
            output += sArr[left]
            left += 1

    return output

 





s = 'aaaaaaa'
s = 'abaac'
s = 'aaaaaaaaaaahgyuejiaagnjdhtyouaaaa'
print(SplitSimilar(s))