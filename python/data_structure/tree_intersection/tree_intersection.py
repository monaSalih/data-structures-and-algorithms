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
#============================
class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        index = self.__hash(key)
        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      index = self.__hash(key)
      if self.__buckets[index]:
          linked_list = self.__buckets[index]
          current = linked_list.head
          while current:
              if current.value[0] == key:
                  return current.value[1]
          current = current.next
      return None

    def contains(self,key):
        idx=self.__hash(key)
        if self.__buckets[idx]:
            return self.__buckets[idx].includes(key)
        else:
            return False
#==============================

def tree_intersection(tree1, tree2):
    arr=[]
    hash = HashTable()
    if tree1.root== None or tree2.root==None:
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



