

"""
Tests for Binary Tree
"""
# Binary_search_tree
from data_structure.trees.trees import (Node,BinaryTree,Binary_search_tree)
import pytest

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

def test_bfs_2():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for A,B,C,D
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "3", "4"]
  # set actual to return value of bfs call
  actual = tree.bfs()
  # assert actual is same as expected
  assert actual == expected
  print("test_bfs_2 passed")



def test_pre_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["1", "2", "4", "3"]
  # set actual to return value of pre_order call
  actual = tree.pre_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_pre_order_ passed")

def test_post_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "3", "1"]
  # set actual to return value of post_order call
  actual = tree.post_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_post_order_ passed")

def test_in_order():
  # Arrange
  # Create tree instance
  tree = BinaryTree()

  # Create Nodes for 1,2,3,4
  a_node = Node('1')
  b_node = Node('2')
  c_node = Node('3')
  d_node = Node('4')
  a_node.left = b_node
  a_node.right = c_node
  b_node.left = d_node

  # Add Root node to tree
  tree.root=a_node

  # set expected list
  expected = ["4", "2", "1", "3"]
  # set actual to return value of in_order call
  actual = tree.in_order()
  # assert actual is same as expected
  assert actual == expected
  print("test_in_order_ passed")



# #================Binary Search Tree Test======================
def test_add():
    """
    add one node to Binary search tree
    """
    tree = Binary_search_tree()
    tree.add('A')
    expected = "A"
    actual = tree.root.data
    assert actual == expected

def test_add_twice():
    """
    add two node to Binary search tree
    """
    tree = Binary_search_tree()
    tree.add('A')
    tree.add('B')
    expected = ["A","B"]
    actual = tree.pre_order()
    assert actual == expected

def test_contains():
    """
    check if node exist in the tree
    """
    tree = Binary_search_tree()
    tree.add('A')
    tree.add('B')
    expected = True
    actual = tree.contains('B')
    assert actual == expected

def test_not_contains():
    """
    check if node not on the tree
    """
    tree = Binary_search_tree()
    tree.add('A')
    tree.add('B')
    expected = False
    actual = tree.contains('E')
    assert actual == expected

def test_contains_exceptions():
    """
    check exceptions
    """
    with pytest.raises(Exception):
        tree=Binary_search_tree()
        actull=tree.contains("O")



#=============================================
# test_bfs()
# test_bfs_2()
# test_pre_order()
# test_in_order()
# test_post_order()
