"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:

  def _init_(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    # Queue breadth <-- new Queue()
    breadth = Queue()
    # breadth.enqueue(root)
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items

    sub method : walk () to make the recursion staff
    """
    list_of_items = []
    def walk(node):
      if node:
        list_of_items.append(node.data)
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)

    walk(self.root)
    return list_of_items


#=================Binary Search Tree Implement=====================

class Binary_search_tree(BinaryTree):

     def add(self, value):

        if not self.root:
            self.root = Node(value)
            # print(self.root.value)
            return

        current = self.root

        while current:
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)

                    return

            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return

     def Contains(self, value):
         if not self.root:
             raise Exception("empty is tree")
         elif value == self.root.value:
             return True
         else:
             current = self.root
             while current:
                 if current.value < value:
                     if current.right:
                         current = current.right
                         if value == current.value:
                            return True
                         else:
                             return False

                 else:

                    if current.left:
                        current = current.left
                        if value == current.value:
                            return True
                    else:
                        return False
