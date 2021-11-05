class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class Ktree :
    def __init__(self):
        self.root=None

    def pre_order(self):
        list_of_item=[]
        def walk(node):
            if node:
                list_of_item.append(node.data)
                if node.left :
                    walk(node.left)
                if node.right :
                    walk(node.right)
        walk(self.root)
        return list_of_item

    def in_order(self):
        list_of_item=[]
        def walk(node):
            if node:
                if node.left :
                    walk(node.left)
                list_of_item.append(node.data)
                if node.right :
                    walk(node.right)
        walk(self.root)
        return list_of_item

    def post_order(self):
        list_of_item=[]
        def walk(node):
            if node:
                if node.left :
                    walk(node.left)
                if node.right :
                    walk(node.right)
                list_of_item.append(node.data)

        walk(self.root)
        return list_of_item

    def fizz_buzz(self):
        if  self.root:
            return "empty empty"
        list_of_item=[]
        def pre_order(root):
            nonlocal list_of_item
            if root.data == None:
                return "empty root"
            if root.data % 3 == 0 and root.data % 5 == 0:
                root.data="fizzbuzz"
                list_of_item += [root.data]
            elif root.data % 3 == 0:
                root.data="fizz"
                list_of_item += [root.data]
            elif root.data % 5 == 0:
                root.data="buzz"
                list_of_item += [root.data]
            if root.left:
                pre_order(root.left)
            if root.right:
                pre_order(root.left)
        return [list_of_item]


