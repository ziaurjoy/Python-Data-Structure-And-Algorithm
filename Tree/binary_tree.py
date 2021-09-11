
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

def create_node():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)

    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)

    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)

    eight = Node(8)
    nine.add_left(eight)

    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)



    return two

def pre_order(node):
    print(node.data)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

def post_order(node):
    if node.left:
        print(post_order(node.left))
    if node.right:
        print(post_order(node.right))
    print(node.data)

def in_order(node):
    if node.left:
        print(in_order(node.left))
    print(node.data)
    if node.right:
        print(in_order(node.right))

if __name__ == "__main__":
    root = create_node()
    # pre_order(root)
    post_order(root)
    # in_order(root)


#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __repr__(self):
#         return repr(self.data)
#
#     def add_left(self, node):
#         self.left = node
#
#     def add_right(self, data):
#         self.right = data
#
#
# def create_tree():
#     two = Node(2)
#     seven = Node(7)
#     nine = Node(9)
#     two.left(seven)
#     two.right(nine)

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data):
        self.left = data

    def add_right(self, data):
        self.right = data

    def __repr__(self):
        return repr(self.data)


def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)

    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)

    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)

    eight = Node(8)
    nine.add_left(eight)

    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    four.add_right(four)

    return two


# def pre_order(node):
#     print(node.data)
#     if node.left:
#         pre_order(node.left)
#     if node.right:
#         pre_order(node.right)

# root = create_tree()
# pre_order(root)


# def post_order(node):
#     if node.left:
#         post_order(node.left)
#     if node.right:
#         post_order(node.right)
#     print(node)
#
# root = create_tree()
# post_order(root)



def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

root = create_tree()
in_order(root)

