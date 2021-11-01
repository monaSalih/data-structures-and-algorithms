# """
# This Module defines a Node and a Binary Tree
# """

# class Node:
#    def __init__ (self,data,left=None,right=None):
#      self.data = data
#      self.left = left
#      self.right = right

# class Queue:
#    def __init__(self, collection=[]):
#      self.data = collection

#    def peek(self):
#      if len(self.data):
#        return True
#      return False

#    def enqueue(self,item):
#      self.data.append(item)

#    def dequeue(self):
#      return self.data.pop(0)

# class BinaryTree:

#    def __init__(self):
#      self.root = None

#    def bfs(self):
#        breadth = Queue()
#        breadth.enqueue(self.root)
#        list_of_items = []
#        while breadth.peek():
#         front = breadth.dequeue()
#         list_of_items += [front.data]

#         if front.left:
#             breadth.enqueue(front.left)

#         if front.right:
#             breadth.enqueue(front.right)

#         return list_of_items

#    def pre_order(self):
#      """
#      A binary tree method which returns a list of items that it contains

#      input: None

#      output: tree items

#      sub method : walk () to make the recursion staff
#      """
#      list_of_items = []
#      def walk(node):
#        if node:
#          list_of_items.append(node.data)
#          if node.left:
#            walk(node.left)
#          if node.right:
#            walk(node.right)

#      walk(self.root)
#      return list_of_items

#    def in_order(self):
#      """
#      function to in order the list using Trees
#      """
#      list_of_items = []
#      def walk(node):
#        if node:
#          if node.left:
#            walk(node.left)
#          list_of_items.append(node.data)
#          if node.right:
#            walk(node.right)

#      walk(self.root)
#      return list_of_items

#    def post_order(self):
#      """
#      A binary tree method which returns a list of items in post order

#      input: None

#      output: tree items
#      """
#      list_of_items = []
#      def walk(node):
#        if node:
#          if node.left:
#            walk(node.left)
#          if node.right:
#            walk(node.right)
#          list_of_items.append(node.data)

#      walk(self.root)
#      return list_of_items


#  =================Binary Search Tree Implement=====================

#  class Binary_search_tree(BinaryTree):
#      root = None

#      def add(self, data):

#          if not self.root:
#              self.root = Node(data)
#               print(self.root.data)
#              return

#          current = self.root

#          while current:
#              if data > current.data:
#                  if current.right:
#                      current = current.right
#                  else:
#                      current.right = Node(data)

#                      return

#              else:
#                  if current.left:
#                      current = current.left
#                  else:
#                      current.left = Node(data)
#                      return

#      def Contains(self, data):
#          if not self.root:
#              raise Exception("empty is tree")
#          elif data == self.root.data:
#              return True
#          else:
#              current = self.root
#              while current:
#                  if current.data < data:
#                      if current.right:
#                          current = current.right
#                          if data == current.data:
#                              return True
#                          else:
#                              return False

#                  else:
#                      if current.left:
#                          current = current.left
#                      if data == current.data:
#                          return True
#                      else:
#                          return False
#   #==========================================

#    def max_number(self):
#             temp=self.root

#             if not self.root:
#                 if temp < self.root:
#                         temp=self.root
#                 elif temp <  temp.left:
#                     temp=temp.left
#                 elif temp <  temp.left:
#                     temp=temp.right
#                 return temp
#             raise Exception("Empty Tree")

# def maximum(self):
#         temp_max=self.root.data
#         if  self.root:
#             if self.root.data> temp_max:
#                 temp_max=self.root.data
#             if self.root.left.data > temp_max:
#                 temp_max = self.root.left.data
#             if self.root.right.data> temp_max:
#                 temp_max = self.root.right.data
#         return [temp_max]

#==============================================================
# def test_max():
#   tree = BinaryTree()
#   a_node = Node('6')
#   b_node = Node('3')
#   d_node = Node('11')
#   c_node = Node('9')

#   a_node.left = b_node
#   a_node.right = c_node
#   c_node.right = d_node
#   tree.root=a_node
#   expected = ["11"]
#   # set actual to return value of post_order call
#   actual = tree.maximum()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_post_order_ passed")
#  def maximum(self):
#         temp_max=self.root.data
#         if  self.root:

#             if self.root.data> temp_max:
#                 temp_max=self.root.data

#             if self.root.left.data > temp_max:
#                 temp_max = self.root.left.data

#             if self.root.right.data> temp_max:
#                 temp_max = self.root.right.data
#         return [temp_max]
# current = self.root
#         # dive to the rightmost leaf
#         while current.right:
#             current = current.right
#         return [current.data]
#=============================================
#==============================================================
# def test_max():
#   tree = BinaryTree()
#   a_node = Node(2)
#   b_node = Node(3)
#   d_node = Node(11)
#   c_node = Node(9)


#   tree.root=a_node
#   tree.root.left=b_node
#   tree.root.right=c_node
#   tree.root.right.right=d_node

#   expected = [11]
#   # set actual to return value of post_order call
#   actual = tree.maximum()
#   # assert actual is same as expected
#   assert actual == expected
#   print("test_post_order_ passed")
