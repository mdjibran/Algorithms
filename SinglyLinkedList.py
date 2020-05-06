class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = new_node

    def length(self):
        curNode = self.head
        l = 0
        while curNode.next != None:
            l += 1
            curNode = curNode.next
        return l

    def show(self):
        els = []
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
            els.append(curNode.data)
        return els

    def delAt(self, index):
        if index >= self.length():
            print("Index out of bound")
            return
        curNode = self.head
        curIdx = 0
        while curNode.next != None:
            last_node = curNode
            curNode = curNode.next
            if curIdx == index:
                last_node.next = curNode.next
                return
            curIdx += 1

n = linkedList()

print(n.show())
print(n.length())
n.append(1)
n.append(4)
n.append(9)
print(n.show())
print(n.length())
n.delAt(1)
print(n.show())
print(n.length())


[0, 1, 4, 9]
curNode = 4
lastNode = 1
