import pytest
from data_structure.trees.trees import BinaryTree,Node
from data_structure.tree_intersection.tree_intersection import common_values
def test_will_return_none():
    tree_one = BinaryTree()
    assert common_values(tree_one, tree_two) == None
def test_return_common_values(tree_one,tree_two):
    assert common_values(tree_one, tree_two) == []
@pytest.fixture
def tree_one():
    one = Node(42)
    two = Node(100)
    three = Node(150)
    four = Node(200)
    five = Node(250)
    six = Node(300)
    seven = Node(350)
    eight = Node(400)
    tree = BinaryTree()
    tree.root =one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    seven.right = eight
    return tree
@pytest.fixture
def tree_two():
    one = Node(42)
    two = Node(50)
    three = Node(70)
    four = Node(100)
    five = Node(250)
    six = Node(300)
    seven = Node(350)
    eight = Node(400)
    tree = BinaryTree()
    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    seven.right = eight
    return tree
