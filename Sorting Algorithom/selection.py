
def selection_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

L = [6, 1, 4, 9, 2]
selection_sort(L)
print(L)





