class Node:
  """
 node class to store value
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

  def __str__(self):
     """
     input:none
     output:{ a } -> { b } -> { c } -> NULL
     action:return formated string represent list value
     """
     input_none = ""
     current = self.head
     while current is not None:
       input_none  +="{"+f' {current.data}'+"}-> "
       current = current.next
     return "{"+f'{current.data}'+"}->Null"
