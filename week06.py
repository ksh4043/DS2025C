from queue import Queue

q1 = Queue()
q1.put("DataBase")
q1.put("Data Structure")
q1.put("Java Script")

print(q1.qsize())
print(q1)
print(q1.get())