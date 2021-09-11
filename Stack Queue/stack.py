

# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
#
# while not s1.is_empty():
#     item = s1.pop()
#     print(item)


# def is_balanced(input_str):
#     s = []
#     for ch in input_str:
#         if ch == "(":
#             s.append(ch)
#         if ch == ")":
#             s.pop()
#     return not s
#
# if __name__ == "__main__":
#     input_str = ")"
#     if is_balanced(input_str):
#         print(input_str, "Is balanced")
#     else:
#         print(input_str, "Is not balanced")






def is_balanced(input_str):
    s = []
    for ch in input_str:
        if ch == "{" and "(" and "[":
            s.append(ch)
        if ch == "}" and ")" and "]":
            s.pop()
    return not s

if __name__ == "__main__":
    input_str = input()
    if is_balanced(input_str):
        print(input_str, "Is balanced")
    else:
        print(input_str, "Is not balanced")











