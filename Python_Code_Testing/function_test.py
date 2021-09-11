# def linear_search(l, x):
#     for i in range(len(l)):
#         if l[i] == x:
#             return i
#     return -1
#
# def test_linear_search():
#     assert -1 == linear_search([1, 2, 3, 4, 5], 7)



# def binary_search(l, x):
#     n = len(l)
#     left = 0
#     right = n-1
#
#     while left <= right:
#         mid = (left+right)//2
#         if l[mid] == x:
#             return mid
#         if l[mid] < x:
#             left = mid + 1
#         if l[mid] > x:
#             right = mid -1
#     return -1
#
# if __name__ == "__main__":
#     l = [1, 2, 3, 5, 6, 7, 8, 9]
#     for x in range(1, 11):
#         position = binary_search(l, x)
#         if position == -1:
#             if x in l:
#                 print(x, "is in l, but function returend -1")
#             else:
#                 print(x, "not in list")
#         else:
#             if l[position] == x:
#                 print(x, "found in correct position")
#             else:
#                 print("Binary search return", position,"for", x, "is incorrect")

# def test_binary_search():
#     assert 4 == binary_search([1, 2, 3, 5, 6, 7, 8, 9], 6)


# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
#
# if __name__ == "__main__":
#
#     s1 = Stack()
#     s1.push(1)
#     s1.push(2)
#     s1.push(3)
#
#     while not s1.is_empty():
#         item = s1.pop()
#         print(item)


#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
# if __name__ == "__main__":
#
#     s1 = Stack()
#     s1.push(1)
#     s1.push(2)
#     s1.push(3)
#
#     while not s1.is_empty():
#         item = s1.pop()
#         print(item)



