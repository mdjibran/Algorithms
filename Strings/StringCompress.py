def conpress(s: str) -> str:
    result = []
    same = 1
    isCompressed = False

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            same += 1
            isCompressed = True
        else:
            result.append(str(s[i-1]))            
            result.append(str(same))
            same = 1

    result.append(s[-1])            
    result.append(str(same))
    if isCompressed:
        return  ''.join(result)
    
    return s



#
print(conpress('aabcccccaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
