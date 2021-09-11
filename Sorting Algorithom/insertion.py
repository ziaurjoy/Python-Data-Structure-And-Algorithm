

def insertion_sort(l):
    n = len(l)
    for i in range(n):
        item = l[i]
        j = i - 1
        while j >= 0 and l[j] > item:
            l[j+1] = l[j]
            j = j-1
            l[j+1] = item



L = [6, 1, 4, 9, 2, 10, 11, 8, 3, 3]
insertion_sort(L)
print(L)


