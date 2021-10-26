class Node:
    def __init__(self,data,next_):
        self.data=data
        self.next=next_
#==============================================stack implement

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def push(self,data):#a  c  b   d   e
        self.top=Node(data,self.top)#a  c  b  d  e
        self.size +=1#1  2  3  4  5

    def pop(self):
        if self.is_empty(): #5
            raise Exception("empty stack")
        result=self.top.data  #e
        self.top=self.top.next #d
        self.size -=1  #4
        return result

    def peek(self):
        if self.is_empty==0:
            raise Exception("empty stack")
        return self.top.data


def Balanced_brackets(item):
    stack=Stack()
    for i in item:
        if i=="{" or i=="[" or i=="(":
            stack.push(i)
        elif i=="}":
            if stack.peek()=="{":
                stack.pop()
            else:
                return False
        elif i=="]":
            if stack.peek()=="[":
                stack.pop()
            else:
                return False
        elif i==")":
            if stack.peek()=="(":
                stack.pop()
            else:
                return False
    if stack.top:
        return False
    else:
        return True


if __name__=="__main__":
    balance=Balanced_brackets("p{hb(ljkjuhyu)}")
    print(balance)
