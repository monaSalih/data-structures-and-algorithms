from _pytest.monkeypatch import V
from _pytest.python_api import raises


class Node:
    def __init__(self,data,next_):
        self.data=data
        self.next=next_
#==============================================stack implement

class Stack:
    def __init__(self):
        self.head=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def push(self,data):#a  c  b   d   e
        self.head=Node(data,self.head)#a  c  b  d  e
        self.size +=1#1  2  3  4  5

    def pop(self):
        if self.is_empty(): #5
            raise Exception("empty stack")
        result=self.head.data  #e
        self.head=self.head.next #d
        self.size -=1  #4
        return result

    def peek(self):
        if self.is_empty==0:
            raise Exception("empty stack")
        return self.head.data

    def peek_next(self):
        if self.is_empty==0:
            raise Exception("empty stack")
        return self.head.next.data

# if __name__=="__main__":
    # stack=Stack()
    # stack.push("a")
    # print(stack.__len__())
    # stack.push("c")
    # stack.push("b")
    # stack.push("d")
    # stack.push("e")
    # top1=stack.top()
    # print(top1)
    # while not stack.is_empty():
    #         stack.pop()
    # print(stack.__len__(),"pop all")
#==============================================queue implement


class Queue:
    def __init__(self) :
        self.head=None
        self.size=0
        self.tail=None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def enqueue (self,value):
        new_node=Node(value,None)
        if self.is_empty():
            self.head=new_node
        else:
            self.tail.next=new_node
        self.tail=new_node
        self.size +=1

    def dequeu(self):
        if self.is_empty():
            raise Exception("is Empty")
        result=self.head.data
        self.head=self.head.next
        self.size -=1
        if self.is_empty():
            self.tail=None
        return result

    def first(self):
        if self.is_empty():
            raise Exception("is Empty")
        return self.head.data


if __name__=="__main__":
    stack=Queue()
    stack.enqueue("a")
    stack.enqueue("c")
    stack.enqueue("b")
    stack.enqueue("d")
    stack.enqueue("e")
    print(stack.__len__())
    stack.dequeu()
    print(stack.__len__())
    print(stack.first())











