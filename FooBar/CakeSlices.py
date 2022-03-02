def solution(s):
    piece = ''
    if len(s)<2: return len(s)
    for i in range(0, len(s)):    # n
        slice = s[i:len(piece)+i] # n
        nxt = s[-len(slice):]
        if slice == piece and slice == nxt:
            return len(s)//len(piece)
        piece += s[i]
    
    return 1





print(solution('aaba'))
#print(solution('abcabcabcabc')) # 4
#print(solution('abccbaabccba')) # 2


#print(solution('abcaacbaabcaacba'))
#print(solution('ababcababc'))
#print(solution('aaaaa'))
#print(solution(''))
# a
# ab
# abc
# abcaddbc
# 