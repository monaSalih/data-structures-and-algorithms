from tree import (Node,BinaryTree)
# """Node"""
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# """BT"""
# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def preOrder(self):
#         output = []

#         def _walk(node):
#             output.append(node.value)
#             if node.left:
#                 _walk(node.left)
#             if node.right:
#                 _walk(node.right)

#         if self.root:
#             _walk(self.root)
#         else:
#             raise AttributeError("Tree is empty.")

#         return output






def FizzOrBuzz(node):
    if node % 3 == 0 and node % 5 == 0:
        return ("FizzBuzz")
    if node % 3 == 0:
        return ("Fizz")
    if node % 5 == 0:
        return ("Buzz")
    else:
        return(str(node))


def FizzBuzzTree(tree):
    fbt = BinaryTree()

    if tree.root == None:
        return fbt

    def _walk(node):
        new_node = Node(FizzOrBuzz(node.value))
        if node.left:
            new_node.left = _walk(node.left)
        if node.right:
            new_node.right = _walk(node.right)
        return new_node

    fbt.root = _walk(tree.root)

    return (fbt)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    fizzBuzzTree = ((FizzBuzzTree(bt)))
    print (fizzBuzzTree.preOrder())
