"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parrent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            self.parrent = node

    def add_right(self, node):
        self.right = node
        if node is not None:
            self.parrent = node


def bst_insert(root, node):
    last_node = None
    current_node = root

    while current_node != None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right

    if current_node == None:
        root = node

    elif current_node.data < last_node.data:
        last_node.add_right(node)
    else:
        last_node.add_left(node)
    return root


def create_best():
    root = TreeNode(10)
    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root, node)
        # print(root)
    return root



# if __name__ == "__main__":
    # root = create_best()
    # print(root)

def bst_search(node, key):
    try:
        while node is not None:

            if node.data == key:
                return node
            if key < node.data:
                node = node.left
            else:
                node = node.right
    except AttributeError:
        pass
    return node


if __name__ == "__main__":
    root = create_best()

    for key in [8, 7]:
        print("Searching", key)
        retult = bst_search(root, key)
        print(retult)

"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parrent = None

    def add_left(self, node):
        self.left = node
        if node is not None:
            self.parrent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            self.parrent = self

    def __repr__(self):
        return repr(self.data)



def bst_insert(root, node):
    current_node = root
    last_node = None
    while current_node is not None:
        last_node = current_node
        if last_node.data > node.data:
            current_node = last_node.left
        else:
            current_node = last_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)

    return root



def bst_create():
    root = TreeNode(10)
    for i in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(i)
        root = bst_insert(root, node)
    return root
root = bst_create()


# def bst_search(node, key):
#     while node is not None:
#         if node.data == key:
#             return node
#         if key < node.data:
#             node = node.left
#         else:
#             node = node.right
#     return node


# for key in [7, 8]:
#     print("Searching key", key)
#     root = bst_create()
#     result = bst_search(root, key)
#     print(result)

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

print(in_order(root))







