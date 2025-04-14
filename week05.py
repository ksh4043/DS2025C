import copy

class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link


    def __str__(self):
        return f"{self.data}"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        # _size : _ 키워드로 히든 필드 네임을 지정 <> private 과는 다른 개념


    def enqueue(self, item):
        self.size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node


    def dequeue(self):
        if self.front is None:
            return "This Queue is Empty"
        self.size -= 1
        temp = self.front
        self.front = self.front.link
        if self.front is None:
            self.rear = None
        return temp.data


    def __str__(self):
        if self.rear is None:
            return "This Queue is Empty"
        for_return_list = []
        current = copy.deepcopy(self.front)
        while current:
            for_return_list.append(str(current))
            current = current.link

        return f"{for_return_list}"


q1 = Queue()
q1.enqueue(55)
q1.enqueue(5)
q1.enqueue(555)
q1.enqueue(5555)

print(q1.size, q1)
print(q1.dequeue())
print(q1.size, q1)
q1.enqueue(100)
print(q1.size, q1)
q1.enqueue("DataBase")
print(q1.size, q1)