class Node:
    def __init__(self,data,next_):
        self.data=data
        self.next=next_

class Queue:
    def __init__(self) :
        self.front=None
        self.rear=None

    def enqueue (self,value):
        new_node=Node(value)
        if not self.front:
            self.front=new_node
            self.rear==new_node
        else:
            self.rear.value


    def dequeu(self):
        if self.front==None:
            raise Exception ("this queue empty")
        dequ_value=self.front
        self.front=self.front.next
        return dequ_value

    def isEmpty(self):
        return self.front == None

    def peek(self):
        if self.front == None:
            return 'Empty Queue'
        return self.front.value





class AnimalShalter:
    def __init__(self):
        self.cat=Queue()
        self.dog=Queue()
        # self.count=0

    def enqueue(self,animal,type):
      if type=='cat' :
        return self.cat.enqueue(animal)
      elif type=='dog' :
        return self.dog.enqueue(animal)
      else :
        return 'This animal cant be in our shelter'

    def dequeue(self,pref):
        if pref =='dog':
            return self.cat.dequeu()
        if pref =='cat':
            return self.cat.dequeu()
        else:
            return 'This animal not exist'

    def is_empty(self):
        if self.count > 0:
            return False
        else:
            return True






if __name__=="__main__":
    catDog=AnimalShalter()
    catDog.enqueue('cat')
    catDog.enqueue('cat')
    catDog.enqueue('dog')
    catDog.enqueue('dog')

    # print(catDog.dequeu('dodg'))
    print(catDog.dequeu('dog'))
    print(catDog.dequeu('dog'))
