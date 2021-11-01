# import data_structure.trees.bfs_trees
from data_structure.trees.bfs_trees import Queue
from data_structure.trees.trees import (Node,BinaryTree)


def test_bfs():
    tree = BinaryTree()
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root=a_node
    expected = ["A", "B", "C", "D"]
    actual = tree.bfs()
    assert actual == expected
    print("test_bfs passed")

def test_empty_bfs():
    tree = BinaryTree()
    expected = None
    actual = tree.bfs()
    assert actual == expected
    print("test_bfs passed")
