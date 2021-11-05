"""Node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        list_of_item = []

        def _walk(node):
            list_of_item.append(node.data)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        if self.root:
            _walk(self.root)
        else:
            return "Tree is empty."

        return list_of_item


def fizzBuzz(node):
    if node % 3 == 0 and node % 5 == 0:
        return ("FizzBuzz")
    if node % 3 == 0:
        return ("Fizz")
    if node % 5 == 0:
        return ("Buzz")
    else:
        return(node)


def fizzBuzzTree(tree):
    game_bt = BinaryTree()

    if tree.root == None:
        return game_bt

    def _walk(node):
        new_node = Node(fizzBuzz(node.data))
        if node.left:
            new_node.left = _walk(node.left)
        if node.right:
            new_node.right = _walk(node.right)
        return new_node

    game_bt.root = _walk(tree.root)

    return (game_bt)


# if __name__ == "__main__":
#     tree_fizz = BinaryTree()
#     tree_fizz.root = Node(2)
#     root_game = tree_fizz.root
#     root_game.right = Node(5)
#     root_game.left = Node(3)
#     root_game.right.left = Node(15)
#     root_game.left.left = Node(10)
#     root_game.right.right = Node(3)
#     fizzBuzzTree = ((fizzBuzzTree(tree_fizz)))
#     print (fizzBuzzTree.pre_order())
