

# def linear_search(l, x):
#     n = len(l)
#     i = 0
#     while i < n:
#         if l[i] == x:
#             return i
#         i += 1
#     return -1
#
# print(linear_search([1, 2, 3, 4, 5], 3))

def linear_search(l, x):
    for i in range(len(l)):
        if l[i] == x:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 7))
