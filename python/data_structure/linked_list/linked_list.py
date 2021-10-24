class Node:
  """
 node class to store data
 pointer to the next value
  """

  def __init__(self, data, next_=None):
    self.data = data
    self.next = next_


class LinkedList:
  """
  linked list class
  need to include head value
  should create empty linked list
  this class should containe 3 method(insert,includes,toString)
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    """"
    input: 1 value
    output:❌
    action:insert new value to the head of the list
    """
    self.head = Node(value, self.head)


  def includes(self, value):
    """
    input: 1 value
    output:true
    action:to check if the value exist in the
    """
    current = self.head
    while current != None:
      if current.data == value:
        return True
      else:
        current = current.next
    return False

  def toString(self):
   '''
  input:none
  output:{ a } -> { b } -> { c } -> NULL
  action:return formated string represent list value

  '''
   string = ""
   current=self.head
   while current != None:
       value = current.data
       if current.next is None:
          string +="{"+f' {value} '+"}" + " -> NULL"
          break

       else:
          string +="{"+f' {value} '+"} -> "
          current = current.next
   return string


  def append(self, value):
     current = self.head
     node=Node(value)
     if current==None:
       self.head = Node(value, self.head)

     while current:
      if current.next==None:
          current.next=node
          node.next=None
          break
      else:
          current=current.next


  def insert_before (self,value,new_data):
      current=self.head
      if self.head==None:
          self.insert(new_data)
      else:
          while current:
              if self.head.next.data==value:
                  data_after=current.next
                  current.next=Node(new_data)
                  current.next.next=data_after
                  break
              current=current.next


  def insert_after (self,value,new_data):
      current=self.head
      while current:
          if current.data==value:
                  next_data=current.next
                  current.next=Node(new_data)
                  Node(new_data).next=next_data
                  break
          current=current.next


# if __name__=="__main__":
#     test=LinkedList()
#     test.insert_after()


