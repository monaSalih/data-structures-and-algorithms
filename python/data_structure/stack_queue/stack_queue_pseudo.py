class Node():
    def __init__(self,value=""):
        self.next=None
        self.value=value

class Stack():
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,value):
       self.top=Node(value)
       self.size +=1

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
        return self.size==0





class Pseudo_Queue:

    def __init__(self):
        self.first_stack=Stack()
        self.secound_stack=Stack()
        self.front=self.first_stack.top
        self.rear=self.secound_stack.top

    def is_empty(self):
        return self.size==0

    def enqueue(self,value):
        self.first_stack.push(value)
        self.rear=self.first_stack.top.value



    def dequeue(self):
        if self.secound_stack.is_empty():
            while self.first_stack.top !=None:
                self.secound_stack.push(self.first_stack.pop())

        return self.secound_stack.pop()

if __name__=="__main__":
    test=Pseudo_Queue()
    test.enqueue(3)
    test.enqueue(4)
    test.enqueue(6)
    test.enqueue(7)
    print(test.dequeue())

