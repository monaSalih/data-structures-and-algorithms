class Node():
    def __init__(self,value=""):
        self.next=None
        self.value=value

class Stack():
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.is_empty():
            raise Exception("empty stack")
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise Exception("empty stack")
        return self.top.value

    def is_empty(self):
     return not self.top

    def __len__(self):
        counter=0
        while self.top:
            counter +=1
            self.pop()
        return counter




class Pseudo_Queue:
    # first_stack=Stack()
    # secound_stack=Stack()
    def __init__(self):
        self.front=None
        self.rear=None
        self.first_stack=Stack()
        self.secound_stack=Stack()


    def enqueue(self,value):
        self.first_stack.push(value)
        self.rear=self.first_stack.top.value


    def dequeue(self):
        if self.is_empty():
            raise Exception("empty equeue")

        self.secound_stack.push(self.first_stack.pop())
        return self.secound_stack.pop()





    def is_empty(self):
     return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter
