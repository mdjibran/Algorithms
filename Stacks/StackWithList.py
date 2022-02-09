def PrintReverse(list: list):
    stack = []

    for e in list:
        stack.append(e)

    
    while stack:
        print(stack.pop())




print( PrintReverse(["a","e","i","o","u"]))