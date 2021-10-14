class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next = next_

class LinkedList:
  """
  A class for creating instances of a Linked List.

  Data and other attributes defined here:

  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None

  def insert(self, value):
    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
    # create new node
    self.head = Node(value, self.head)

  def include(self,value ):
        current=self.head
        # bool_result=False
        while current is False:
            if current.value==value:
                return True
            else:
                current=current.next
        return False

  def toString(self):
        input_none = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                input_none  +=f"( {value} ) -> NULL"
                break
            input_none  += f"( {value} ) -> "
            current = current.next
            return input_none





