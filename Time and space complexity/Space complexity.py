

# n = int(input())
#
# if n % 2 == 0: # Space complexity is O(1)
#     print(n, "Is even number")
# else:
#     print(n, "Is odd number")


# n = int(input())
# even = [False] * (n+1) # Space complexity is O(n)
# for i in range(0, n+1, 2):
#     even[i] = True
# print(even)


# n = int(input())
# count = 0
# for i in range(n):
#     for j in range(n): # Complexity O(n^2)
#         count += 1
# print(count)




# n = int(input())
# count = 0
# for i in range(n):
#     for j in range(n):
#         for k in range(n): # Complexity O(n^3)
#             count += 1
# print(count)


n = int(input())
count = 0

for i in range(n): # Complexity 0(n)
    count += 1

for i in range(n):
    for j in range(n): # Complexity O(n^2)
        # """
            # O(n+n^2) = O(n^2)
        # """
        count += 1
print(count)
