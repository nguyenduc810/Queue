class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def Enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty() :
            self.head = self.tail = newNode
            self.size += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    '''def Dequeue(self):
        if self.isEmpty():
            return
        self.Info = self.head.data
        self.head = self.head.next
        self.size -=1
        return self.Info  '''
q = Queue()
q.Enqueue(1)
q.Enqueue(2)
print(q.head.data)


