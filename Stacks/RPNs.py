def PerformOperation(v1, v2, opr):
    if opr == '+':
        return v1 +v2
    elif opr == '-':
        return v1 - v2
    elif opr == '*':
        return v1 * v2
    elif opr == '/':
        return v1 / v2
    
    return -1


def CalculateRPN(lst: str):
    stk = []

    for e in lst.split(','):
        print(stk)
        if e not in ['+','-','*','/']:
            stk.append(int(e))
        else:
            v1 = stk.pop()
            v2 = stk.pop()
            result = PerformOperation(v2, v1, e)
            stk.append(result)
    
    return stk.pop()




#print(CalculateRPN("3,4,+,2,*,1,+"))