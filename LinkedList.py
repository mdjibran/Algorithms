class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        print(total)

    def display(self):
        elms = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elms.append(cur.data)
        print(elms)

ll = Linked_list()
ll.append(12)
ll.display()
ll.length()

ll.append(4)
ll.append(8)
print(ll)
