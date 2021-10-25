class Node:
    def __init__(self,data,next_):
        self.data=data
        self.next=next_

class Queue:
    def __init__(self) :
        self.front=None
        self.size=0
        self.rear=None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def enqueue (self,value):
        new_node=Node(value,None)
        if self.is_empty():
            self.front=new_node
        else:
            self.rear.next=new_node
        self.rear=new_node
        self.size +=1

    def dequeu(self):
        if self.is_empty():
            raise Exception("is Empty")
        result=self.front.data
        self.front=self.front.next
        self.size -=1
        if self.is_empty():
            self.tail=None
        return result

    def peek(self):
        if self.is_empty():
            raise Exception("is Empty")
        return self.front.data

class AnimalShalter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()

    def enqueue(self,animal):
      if animal=='cat' :
        self.cat.enqueue(animal)

      elif animal=='dog' :
        self.dog.enqueue(animal)

      else :
        return 'This animal not exist'

    def dequeue(self,animal):
        if animal =='dog':
            return self.cat.dequeue()
        if animal =='cat':
            return self.dog.dequeue()
        else:
            return 'This animal not exist'

        






if __name__=="__main__":
    catDog=AnimalShalter()
    catDog.enqueue('cat')
    catDog.enqueue('cat')
    catDog.enqueue('dog')
    catDog.enqueue('dog')

    # print(catDog.dequeue('dodg'))
    print(catDog.dequeue('dog'))
    print(catDog.dequeue('dog'))
