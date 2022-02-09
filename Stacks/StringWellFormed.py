def CheckifWellFormed(s: str):
    stk = []
    bracketSet = {'(':')', '[':']', '{':'}'}

    for b in s.split(','):
        if b in bracketSet:
            stk.append(b)
        else:
            if len(stk) > 0:
                lastB = stk[-1]
                closeB = bracketSet[lastB]
                if closeB == b:
                    stk.pop()
    
    return len(stk) == 0








print(CheckifWellFormed(""))