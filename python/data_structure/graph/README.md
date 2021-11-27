# Graphs
<!-- Short summary or background information -->
A Graph is a non-linear data structure consisting of nodes and edges.
## Challenge
<!-- Description of the challenge -->
* add node
Arguments: value
Returns: The added node
* add edge
Arguments: 2 nodes to be connected by the edge
Returns: nothing
* get nodes
Arguments: none
Returns all of the nodes in the graph as a collection

* get neighbors
Arguments: node
Returns a collection of edges connected to the given node

* size
Arguments: none
Returns the total number of nodes in the graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* add node:
Time:O(1)
space:O(1)

* add edge:
Time:O(1)
space:O(1)

* get nodes:
Time:O(1)
space:O(1)

* get neighbors:
Time:O(1)
space:O(1)

* size:
Time:O(1)
space:O(1)
## API
<!-- Description of each method publicly available in your Graph -->
```
class Graph:
  def __init__(self):
    """
    Initalization for a hashmap to hold the vertices
    """
    self.__adjacency_list = {}

  def add_node(self, value):
    """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
    # new node
    v = Vertex(value)
    self.__adjacency_list[v] = []
    return v

  def size(self):
    return len(self.__adjacency_list)

  def add_edge(self, start_vertex, end_vertex, weight=0):
    """Adds an edge to the graph"""
    if start_vertex not in self.__adjacency_list:
      raise KeyError("Start Vertex not found in graph")

    if end_vertex not in self.__adjacency_list:
      raise KeyError("End Vertex not found in graph")

    edge = Edge(end_vertex, weight)
    self.__adjacency_list[start_vertex].append(edge)

  def get_nodes(self):
    """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
    return self.__adjacency_list.keys()

  def get_neighbors(self, vertex):
    """ """
    return self.__adjacency_list.get(vertex, [])

```
