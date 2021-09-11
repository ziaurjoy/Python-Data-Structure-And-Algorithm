# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         nodes = []
#         current_node = self.head
#         while current_node:
#             nodes.append(current_node.data)
#             current_node = current_node.next
#         return nodes
#
#     def append(self, new_node):
#         node = Node(new_node)
#         if self.head.next is None:
#             self.head = node
#         current_node = self.head.next
#         while current_node.next:
#             current_node = current_node.next
#         current_node.next = node
#
#     def prepend(self, new_node):
#         node = Node(new_node)
#         node.next = self.head
#         self.head = node
#         return self.head
#
#     def insert(self, node_number, new_node):
#         current_node = self.head.next
#         while current_node:
#             if current_node.data == node_number:
#                 node = Node(new_node, current_node.next)
#                 current_node.next = node
#                 break
#             current_node = current_node.next
#
#     def search(self, search_node):
#         current_node = self.head.next
#         while current_node:
#             if current_node.data == search_node:
#                 return current_node
#             current_node = current_node.next
#         return None
#
#     def remove(self, remove_node):
#         if self.head.data == remove_node:
#             self.head = self.head.next
#
#         prev = None
#
#         current_node = self.head
#
#         while current_node and current_node.data != remove_node:
#             prev = current_node
#             current_node = current_node.next
#         if current_node:
#             prev.next = current_node.next
#
#
#
# a = LinkedList()
# a.prepend(1)
# a.prepend(2)
# a.prepend(3)
# a.append(6)
# a.insert(2, 5)
# a.remove(3)
# print(a.print())





class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DouplyLinklist:
    def __init__(self):
        self.head = Node()

    def print(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return nodes

    def append(self, data):
        node = Node(data)
        if self.head.next == None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        if current_node:
            current_node.next = node
            node.prev = current_node

    def prepend(self, data):
        current_node = self.head.next
        new_node = Node(data, None, current_node)
        self.head.next = new_node
        if current_node:
            current_node.prev = new_node

    def search_node(self, data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next


    def remove(self, item):
        node = self.search_node(item)
        if node is None:
            return

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        if node.next:
            node.next.prev = node.prev


# a = DouplyLinklist()
# a.append(1)
# a.append(2)
# a.prepend(4)
#
# print(a.print())
# a.remove(2)
# print(a.print())
#
# def test_append():
#     dll = DouplyLinklist()
#     assert dll.head.next == None, "Linked list empty, so head should point to None"
#
#     item = 5
#     dll.append(5)
#     assert dll.head.next.data == item, "Head should point to the first node"
#
#     second_item = 8
#     dll.append(second_item)
#     assert dll.head.next.data, "Head should point to the first node"
#
#     first_node = dll.head.next
#     second_node = first_node.next
#     assert first_node.next.data == second_item, "first node should point to second node"
#
#     assert second_node.prev.data == item, "Previous node of second should be the first node"
#
# def test_prepend():
#     dell = DouplyLinklist()
#     assert dell.head.next == None, "Linked list empty, so head should point to None"
#
#     item = 5
#     dell.prepend(5)
#     assert dell.head.next.data == item, "head should point to the first node"
#
#     new_item = 10
#     dell.prepend(new_item)
#     assert dell.head.next.data == new_item, "Head should point to the new node"
#
# def test_remove():
#     dll = DouplyLinklist()
#     dll.append(5)
#     dll.append(10)
#     dll.append(15)
#     dll.append(20)
#
#     node_5 = dll.search_node(5)
#     node_10 = dll.search_node(10)
#     node_15 = dll.search_node(15)
#     node_20 = dll.search_node(20)
#
#     assert node_10.next == node_15
#     assert node_15.prev == node_10



# list_a = [1, 2, "Joy"]
# print(hex(id(list_a)))
# print(id(list_a[1]))
# print(id(list_a[1]))


