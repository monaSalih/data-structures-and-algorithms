
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
#=================BFEs=========================
def test_bfs():
    tree = BinaryTree()
    a_node = Node(2)
    b_node = Node(7)
    c_node = Node(5)#right root
    d_node = Node(2)
    e_node = Node(6)
    f_node = Node(9)
    g_node = Node(5)
    h_node = Node(11)
    i_node = Node(4)
#==========node location============
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    e_node.left=g_node
    e_node.right=h_node
    c_node.right=f_node
    f_node.left=i_node
#==========node location End============
    tree.root=a_node
    expected = [2,7,5,2,6,9,5,11,4]
    actual = tree.bfs()
    assert actual == expected
    print("test_bfs passed")
#=============================================
# test_bfs()
# test_bfs_2()
# test_pre_order()
# test_in_order()
# test_post_order()
