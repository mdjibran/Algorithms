from inspect import stack
from re import S
import sys

class Stack:

    stk = []
    maxIdx = -1
    maxVal = -sys.maxsize

    def Push(self, v):
        self.stk.append(v)
        self.storeMaxIdx(v, self.maxIdx+1)


    def Pop(self):
        if len(self.stk) > 0:
            v = self.stk.pop()
            self.storeMaxIdx(v, self.maxIdx - 1)
            return 

    def storeMaxIdx(self, newVal, newIdx):
        if(newVal > self.maxVal):
            self.maxVal = newVal
            self.maxIdx = newIdx

    def Peek(self):
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            False

    def Max(self):
        return self.maxVal



s = Stack()
print(s.Max())

s.Push(2)
s.Push(10)
s.Push(1)

print(s.Max())
print(s.Peek())
