

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
# print(binary_search([1, 2, 3, 5, 6, 7, 8, 9], 6))


def binary_search(l, x):
    n = len(l)
    left = 0
    right = n-1
    for i in range(left, right):
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        if l[mid] < x:
            left = mid + 1
        if l[mid] > x:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 5, 6, 7, 8, 9], 6))
