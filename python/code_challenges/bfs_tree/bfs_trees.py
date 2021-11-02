from data_structure.trees.trees import (Node,Queue,BinaryTree)



def bfs(self):
        """

        """
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
