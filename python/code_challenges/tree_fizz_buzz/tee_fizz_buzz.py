"""Node"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.middle = None
        self.middle_left = None
        self.middle_right= None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None
        self.list_of_item=[]

    def walk(self, node):
        self.list_of_item.append(node.data)
#test new branch
        if node.left:
            self.walk(node.left)
        if node.middle:
            self.walk(node.middle)
        if node.right:
            self.walk(node.right)


    def pre_order(self):
        if self.root:
            self.walk(self.root)
        else:
            return "Tree is empty."

        return self.list_of_item


def fizzBuzz(value):
    if value % 3 ==0 and value % 5 ==0 :
        return "fizzBuzz"
    if value % 3 ==0 :
        return "fizz"
    if value % 5 ==0 :
        return "buzz"
    else :
        return value




def fizzBuzzTree(tree):

    # k-tree 4tree
    game_bt = BinaryTree()

    if tree.root == None:
        return game_bt

    def _walk(node):
        new_node = Node(fizzBuzz(node.data))
        if node.left:
            new_node.left = _walk(node.left)
        if node.middle:
            new_node.middle = _walk(node.middle)
        if node.right:
            new_node.right = _walk(node.right)
        return new_node

    game_bt.root = _walk(tree.root)

    return (game_bt)


if __name__ == "__main__":
    tree_fizz = BinaryTree()
    tree_fizz.root = Node(2)
    root_game = tree_fizz.root
    root_game.right = Node(5)
    root_game.middle = Node(21)
    root_game.left = Node(3)

    root_game.right.left = Node(15)
    root_game.left.left = Node(10)

    root_game.middle.left = Node(21)
    root_game.middle.right = Node(5)

    root_game.right.right = Node(3)
    fizzBuzzTree = fizzBuzzTree(tree_fizz)
    print (fizzBuzzTree.pre_order())
