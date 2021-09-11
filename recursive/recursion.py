#
#
# def factorial(n):
#     if n < 0:
#         return None
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n-1)
#
# def test_factorial():
#     assert factorial(1) == 1
#     assert factorial(0) == 1
#     assert factorial(-1) == None
#     assert factorial(5) == 120
# # print(factorial(5))
#
#
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#
# def test_fibonacci():
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
#     assert fibonacci(4) == 3
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8
# print(fibonacci(4))
#
#
#
# li = [1, 1, 2, 3, 5, 8, 13]
# for key, value in enumerate(li):
#     print(key, value)
#
#
#
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#
# def test_fibonacci():
#     fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     for n, f in enumerate(fib):
#         assert fibonacci(n+1) == f
#
#
# print("\n")
# print("Hello")
#
# def print_number(n):
#     if n== 0:
#         return
#     print(n)
#     print_number(n-1)
#
# if __name__ == "__main__":
#     print_number(5)
#
# print("\n")
# def print_number(n):
#     if n==0:
#         return
#     print_number(n-1)
#     print(n)
# if __name__ == "__main__":
#     print_number(5)



def binary_search_recursive(l, left, right, x):

    if right < 0:
        return -1
    mid = (left + right)//2
    if l[mid] == x:
        return mid
    if l[mid] < x:
        return binary_search_recursive(l, mid+1, right, x)
    else:
        return binary_search_recursive(l, left, mid-1, x)

print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8],0, 8, 5))




