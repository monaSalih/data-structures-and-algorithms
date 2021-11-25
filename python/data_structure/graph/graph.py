from collections import deque

class Vertex:
  def __init__(self, value):
    """

    """
    self.value =value

class Queue:
  def __init__(self):
    self.dq=deque()
    def enqueue(self,value):
      self.dq.append(value)

    def dequeue(self):
      self.dq.pop()


class Stack:
  def __init__(self):
    self.dq=deque()

  def push(self,value):
    self.dq.append(value)

  def pop (self):
    self.dq.pop()

class Edge:
  def __init__(self,vertix,weight):
    self.vertix=vertix
    self.weight=weight


class Graph:
  def __init__(self):
    self.__adjacancey_list={}

  def add_node(self,value):
    v= Vertex(value)
    self.__adjacancey_list[v]=[]
    return v

  def size(self):
    return len(self.adjacancey_list)

  def add_edge(self,start_vertex,end_vertex,weight=0):
    # if
    edge =Edge (end_vertex,weight)
    self.____adjacancey_list[start_vertex].append(edge)

  def get_node(self):
    return self.____adjacancey_list.keys()

  def get_neighbors(self, vertex):
    return self.____adjacancey_list.get(vertex, [])

  def breadth_first_search(self,start_vertex, action=()):
    queue =Queue()
    visited = set()
