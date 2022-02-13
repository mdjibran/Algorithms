from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()
    
    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()

    def maxInQ(self):
        return max(self.data)

    def show(self):
        print("#####")
        for e in self.data:
            print(e)


q = Queue()

q.enqueue(3)
q.enqueue(9)
q.show()
q.enqueue(2)
q.enqueue(6)
q.show()
print(q.maxInQ())