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

    # def is_empty(self):
    #  return not self.top

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
        self.first_stack=Stack()
        self.secound_stack=Stack()
        self.front=self.first_stack.top
        self.rear=self.secound_stack.top

    def is_empty(self):
        return self.size==0

    def enqueue(self,value):
        node=Node(value)
        node.next=self.front
        self.next=self.front
        self.first_stack.push(node)
        self.size +=1
        # return self.rear



    def dequeue(self):
        if self.secound_stack.is_empty():
            while not self.first_stack.is_empty():
                self.secound_stack.push(self.first_stack.pop())
        return self.secound_stack.pop().data





    # def is_empty(self):
    #  return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter

if __name__=="__main__":
    stack=Pseudo_Queue()
    stack.enqueue("a")
    stack.enqueue("c")
    stack.enqueue("b")
    stack.enqueue("d")
    stack.enqueue("e")
    print(stack.__len__())
    # stack.dequeu()
    # print(stack.__len__())
    # print(stack.front())
