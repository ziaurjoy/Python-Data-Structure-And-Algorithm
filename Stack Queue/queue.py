

# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def dequeue(self):
#         return self.items.pop(0)
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
# s1 = Queue()
# s1.enqueue("Joy")
# s1.enqueue("Salam")
# s1.enqueue("Kabir")
# s1.enqueue("Bangladesh")
#
# while not s1.is_empty():
#     item = s1.dequeue()
#     print(item)




#
# class Queue:
#     def __init__(self, size):
#         self.items = [0] * size
#         self.max_size = size
#         self.head = 0
#         self.tail = 0
#         self.size = 0
#
#     def enqueue(self, item):
#         if self.is_full():
#             print("Queue is full")
#             return
#         print("Insert", item)
#         self.items[self.tail] = item
#         self.tail = (self.tail+1) % self.max_size
#         self.size += 1
#
#     def dequeue(self):
#         item = self.items[self.head]
#         self.head = (self.head+1) % self.max_size
#         self.size -= 1
#         return item
#
#     def is_full(self):
#         if self.size == self.max_size:
#             return True
#         return False
#
#     def is_empty(self):
#         if self.size == 0:
#             return True
#         return False
#
#
# if __name__ == "__main__":
#     q = Queue(4)
#     q.enqueue("Joy")
#     q.enqueue("Bangla")
#     q.enqueue("Bangladesh")
#     # q.enqueue("Ziaur")
#     print(q.items)

