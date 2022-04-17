# This problem was asked by Google.
#
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

# library for providing C
# compatible data types
import ctypes


# Node class for memory
# efficient doubly linked list
class Node:

    def __init__(self, data):
        self.data = data

        # XOR of next and previous node
        self.npx = 0


class XorLinkedList:

    def __init__(self):

        self.head = None
        self.__nodes = []

    # Returns XORed value of the node addresses
    def xor(self, a, b):

        return a ^ b

    # Insert a node at the beginning of the
    # XORed linked list and makes the newly
    # inserted node as head
    def insert_at_start(self, data):

        node = Node(data)

        # Since new node is being inserted at
        # the beginning, npx of new node will
        # always be XOR of current head and NULL
        node.npx = id(self.head)

        # If linked list is not empty, then
        # npx of current head node will be
        # XOR of new node and node next to
        # current head
        if self.head is not None:
            # head.npx is XOR of None and next.
            # So if we do XOR of it with None,
            # we get next
            self.head.npx = self.xor(id(node),
                                     self.head.npx)

        self.__nodes.append(node)

        # Change head
        self.head = node

    # Prints contents of doubly linked
    # list in forward direction
    def print_nodes(self):

        if self.head != None:
            prev_id = 0
            curr = self.head
            next_id = 1

            print("Following are the nodes "
                  "of Linked List:")

            while curr is not None:
                # Print current node
                print(curr.data, end=' ')

                # Get address of next node: curr.npx is
                # next^prev, so curr.npx^prev will be
                # next^prev^prev which is next
                next_id = self.xor(prev_id, curr.npx)

                # Update prev and curr for next iteration
                prev_id = id(curr)
                curr = self.__type_cast(next_id)

    # Method to return a new instance of type
    # which points to the same memory block.
    def __type_cast(self, id):

        return ctypes.cast(id, ctypes.py_object).value


# Driver code
if __name__ == '__main__':
    obj = XorLinkedList()

    # Create following Doubly Linked List
    # head-->40<-->30<-->20<-->10
    obj.insert_at_start(10)
    obj.insert_at_start(20)
    obj.insert_at_start(30)
    obj.insert_at_start(40)

    # Print the created list
    obj.print_nodes()
