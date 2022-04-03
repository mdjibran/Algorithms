

class Stack():
    

    def __init__ (self):
        self.stk = []

    def Push(self, e: int):
        self.stk.append(e)

    def Pop(self) -> int:
        return self.stk.pop()
    
    def Peek(self) -> int:
        if len(self.stk) > 0:
            return self.stk[-1]
        return 
    
    def Display(self):
        return self.stk
    


class MinStack:
    numStack = Stack()
    minStack = Stack()

    def Push(self, e: int):
        minV = e
        if len(self.minStack.Display()) > 0:
            minV = min(self.minStack.Peek(), e)
        self.minStack.Push(minV)
        self.numStack.Push(e)

    def Pop(self) -> int:
        self.minStack.Pop()
        return self.numStack.pop()
    
    def Peek(self) -> int:
        return self.numStack.Peek()
    
    def Display(self):
        return self.numStack.Display()

    def DisplayMinStack(self):
        return self.minStack.Display()

    def GetMin(self) -> int:
        return self.minStack.Peek()

o = MinStack()
o.Push(10)
o.Push(2)
o.Push(6)
print(o.Display())
print(o.DisplayMinStack())
print(o.GetMin())
