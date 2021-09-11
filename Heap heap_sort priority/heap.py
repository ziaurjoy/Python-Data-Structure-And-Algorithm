#
#
# heap = [None] * 10
# heap[1] = 19
# heap[2*1] = 7
# heap[2*1+1] = 17
# heap[2*2] = 3
# heap[2*2+1] = 5
# heap[3*2] = 12
# heap[3*2+1] = 10
# heap[4*2] = 1
# heap[4*2+1] = 2
# # print(heap)
#
# def left(i):
#     return 2 * i
#
# def right(i):
#     return 2 * i + 1
#
# def parent(i):
#     return i//2

# print(left(3))


# def is_max_heap(h):
#     n = len(h) - 1
#     for i in range(n, 1, -1):
#         parent_node = parent(i)
#         if h[parent_node] < h[i]:
#             return False
#     return True
#
# h = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
# print(h, is_max_heap(h))



# def is_min_heap(list):
#     n = len(list) - 1
#     for i in range(n, 1, -1):
#
#         def parent(i):
#             return i // 2
#
#         parent_node = parent(i)
#         if list[parent_node] > list[i]:
#             return False
#     return True
#
# heap = [None, 1, 2, 3, 17, 19, 36, 7, 25, 100]
# print(heap, is_min_heap(heap))
#
# h = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
# print(h, is_min_heap(h))


def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

if __name__ == "__main__":
    # h = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    # print(h)
    # max_heapify(h, 9, 3)
    # print(h)
    # print()
    h = [None, 1, 2, 3]
    print(h)
    max_heapify(h, 3, 1)
    print(h)

