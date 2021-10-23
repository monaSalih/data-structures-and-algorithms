class Node:
  """
 node class to store data
 pointer to the next value
  """

  def __init__(self, data, next_=None):
    self.data = data
    self.next = next_
# ================================================

class LinkedList:
  """
  linked list class
  need to include head value
  should create empty linked list
  this class should containe 3 method(insert,includes,toString)
  """
# ================================================
  def __init__(self):
    self.head = None #head[data,next]

  def insert(self, value):
    """"
    input: 1 value
    output:❌
    action:insert new value to the head of the list
    """
    self.head = Node(value, self.head)
# ================================================

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
# ================================================
  def __str__(self):
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

# ================================================
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

# ================================================
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
# ================================================

  def insert_after (self,value,new_data):
      current=self.head
      while current:
          if current.data==value:
                  next_data=current.next
                  current.next=Node(new_data)
                  Node(new_data).next=next_data
                  break
          current=current.next
# ================================================
  def kth(self,k):
        if k<0:
          return "Exception"
        current=self.head
        counter=0
        while current:

            if current.next == None:
                current=self.head
                break
            else:
                counter +=1
                current =current.next
        print(counter)
        value_postion=counter-k
        if k>counter:
            return "Exception"
        counter=0
        while current:
             if current.next == None:
               pass
             elif counter ==value_postion:
                 return current.data
             else:
                counter +=1
                current=current.next
# ================================================
#   def palindrome(self):
#     node = self.head
#     length = 0
#     comp = []
#     while node:
#       comp.append(node.data)
#       node = node.next
#       length += 1
#     node = self.head
#     for item in comp[::-1]:
#       if (item!= node.data):
#         return False
#       node = node.next
#     return True

# ================================================


# ================================================




if __name__=="__main__":
    # test=LinkedList()
    # test.append(1)
    # test.append(3)
    # test.append(8)
    # test.append(2)
    # print(test.kth(2),test.kth(6),test.kth(6),test.kth(1))
    # print(test.__str__())
    #====================================
    list1=LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    

# if __name__=="__main__":
#     test=LinkedList()
#     test.insert_after()


