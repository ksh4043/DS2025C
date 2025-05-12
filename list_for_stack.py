# class Queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#
#     def enqueue(self, item):
#         while len(self.s1) != 0:
#             self.s2.append(self.s1.pop())
#         self.s1.append(item)
#         while len(self.s2) != 0:
#             self.s1.append(self.s2.pop())
#
#
#     def dequeue(self):
#         if len(self.s1) == 0:
#             return "This Queue is Empty"
#         return self.s1.pop()
#
#
#
# q = Queue()
# q.enqueue(55)
# q.enqueue(125)
# q.dequeue