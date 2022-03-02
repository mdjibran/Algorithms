def URLify(s: str, trueLength: int) -> str:
    pointer = len(s) - 1
    waitingFirstChar = True
    workingIdx = pointer
    lst = [' ' for s in range(len(s))]

    while pointer >= 0:
        c = s[pointer]
        if waitingFirstChar and c == ' ':
            pointer -= 1

        else:
            waitingFirstChar = False
            if c == ' ':
                lst[workingIdx] = '0'
                lst[workingIdx-1] = '2'
                lst[workingIdx-2] = '%'
                workingIdx -= 3
            else:
                lst[workingIdx] = s[pointer]
                workingIdx -= 1
            
            pointer -= 1

    return ''.join(lst)





s = 'Mr John Smith      '
print(URLify(s, 13))