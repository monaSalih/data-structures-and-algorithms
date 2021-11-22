from hash_table.hash_table import *
from trees.trees import *


def tree_intersection(tree1, tree2):
    arr=[]
    hash = HashTable()
    if tree1.root== None or tree.root==None:
        return 'input tree is empty'
    def walk(node:Node):
        if node:
            hash.add(str(node.data),None)
        if node.left:
            walk(node.left)
        if node.right:
            walk(node.right)
    walk(tree1.root)
    def walk2(node:Node):
        if node:
            if hash.contains(str(node.data)):
                arr.append(node.data)
        if node.left:
            walk2(node.left)
        if node.right:
            walk2(node.right)
        return arr
    return walk2(tree2.root)



