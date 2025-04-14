import copy

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


    def __str__(self):
        return f"{self.data}"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0


    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if self.front is None:
            return "This Queue is Empty"
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data


    def size(self):
        return self._size


    def __str__(self):
        if self.front is None:
            return "This Queue is Empty"
        for_return_list = []
        current = copy.deepcopy(self.front)
        while current:
            for_return_list.append(str(current))
            current = current.next

        return f"{for_return_list}"


q1 = Queue()
q2 = Queue()
q1.enqueue(55)
q1.enqueue(5)
q1.enqueue(555)
q1.enqueue(5555)

print(q1)
print(q2)
print(q1.size())

q1.enqueue(100)
print(q1)