from code_challenges.tree_fizz_buzz.tee_fizz_buzz import (Node,BinaryTree,fizzBuzz,fizzBuzzTree)

def test_fizzbuzztree():
    tree_fizz = BinaryTree()
    tree_fizz.root = Node(2)
    root_game = tree_fizz.root
    root_game.right = Node(5)
    root_game.left = Node(3)
    root_game.right.left = Node(15)
    root_game.left.left = Node(10)
    root_game.right.right = Node(3)
    fizz_buzz_tree = fizzBuzzTree(tree_fizz)
    actual = fizz_buzz_tree.pre_order()
    excepted = [2, 'Fizz', 'Buzz', 'Buzz', 'FizzBuzz', 'Fizz']
    assert actual == excepted


