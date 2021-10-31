class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Queue:
    def __init__(self,collection=[]) :
        self.data=collection
    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self,value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

class BinaryTree:
    def __init__(self):
        self.root=None

    def bfs(self):
        breadth=Queue()
        breadth.enqueue(self.root)
        list_of_item=[]

        while breadth.peek():
            front=breadth.dequeue()
            list_of_item += [front.data]

            if front.left :
                breadth.enqueue(front.left)
            if front.right :
                breadth.enqueue(front.right)
        return list_of_item

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
#=============================================
    def maximum(self):
            temp_max=self.root.data
            if  self.root:

                if self.root.data> temp_max:
                    temp_max=self.root.data

                if self.root.left.data > temp_max:
                    temp_max = self.root.left.data

                if self.root.right.data> temp_max:
                    temp_max = self.root.right.data
            return [temp_max]
# current = self.root
#         # dive to the rightmost leaf
#         while current.right:
#             current = current.right
#         return [current.data]
#=============================================
class Binary_search_tree(BinaryTree):
    def __init__(self):
        super().__init__()

    def bfs(self):
        breadth=Queue()
        breadth.enqueue(self.root)
        list_of_item=[]

        while breadth.peek():
            front=breadth.dequeue()
            list_of_item += [front.data]

            if front.left :
                breadth.enqueue(front.left)
            if front.right :
                breadth.enqueue(front.right)
        return list_of_item
    def add(self,value):
        if not self.root:
            self.root = Node(value)

        else:
            temp=self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left=Node(value)
                        break
                    temp=temp.left
                else:
                    if not temp.right:
                        temp.right=Node(value)
                        break
                    temp=temp.right
    def contains(self,value):
        if not self.root:
            raise Exception("Empty Tree")
        else:
            temp=self.root
            while temp:
                if value == temp.data:
                    return True
                elif value < temp.data:
                    if not temp.left:
                        return False
                    temp=temp.left
                else:
                    if not temp.right:
                        return False
                    temp=temp.right





if __name__=="__main__":
    tree = BinaryTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root=a_node
    print(tree.maximum())
