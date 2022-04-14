# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class:
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    val = node.val
    left = serialize(node.left) if node.left else None
    right = serialize(node.right) if node.right else None
    return [val, left, right]


def deserialize(serialized_node):
    val = serialized_node[0]
    left = deserialize(serialized_node[1]) if serialized_node[1] else None
    right = deserialize(serialized_node[2]) if serialized_node[2] else None
    return Node(val, left, right)


tree = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(tree)).left.left.val == "left.left"
