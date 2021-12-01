from collections import deque


class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """

    def __init__(self, value):
        """
        Initalization for a Vertex to hold a value.

        """
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendLeft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
                    The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
                    """
        self.dq = deque()

    def push(self, value):
        """
                    Store the passed value in a node and then push the node on top of the stack.

                    PARAMETERS
                    ----------
                            value: any
                                    The value that will get stored in a node to be pushed on top of the stack.
                    """
        self.dq.append(value)

    def pop(self):
        """
                    Return the top node in a stack.
                    """
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Edge:
    """
      a class for Adding a new edge between two nodes in the graph
      If specified, assigning a weight to the edge
      Arguments: 2 nodes to be connected by the edge, weight (optional)
      Returns: nothing

    """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


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

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)

            neighbors = self.get_neigbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbors not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbors)

    def depth_first(self, start_vertex):
        vertex = []
        visited = []
        stack = Stack()

        if start_vertex not in self.__adjacency_list:
            raise KeyError(' not exist in graph')

        visited.append(start_vertex)
        stack.push(start_vertex)

        while len(stack):
            vertex_stack = stack.pop()
            vertex.append(vertex_stack)
            vertex_neighbors = self.get_neighbors(vertex_stack)

        for neighbor in vertex_neighbors:
            if neighbor.weight not in visited:
                visited.append(neighbor.weight)
                stack.push(neighbor.weight)
        return str(vertex_stack[0])

    def graph_depth_first(self,vertex):
         depth=[]
         depth_list=[]
         depth_list.append(vertex)
         while (len(depth_list)):
             edges=self.get_neighbors(vertex)
             if len(edges):
                 for i in edges:
                     if not i.vertex in depth_list:
                         depth_list.append(i.vertex)
         return depth








if __name__ == '__main__':
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')

    graph.add_edge(node_a, node_c, 5)
    graph.add_edge(node_a, node_c, 5)
    graph.add_edge(node_b, node_c, 1)

    graph.get_nodes()

    # graph.get_neighbors(node_a) [0].weight
    # graph.get_neighbors (node_b)[0].weight
    # graph.get_neighbors (node_c)[0].weight
    # graph.get_neighbors (node_d)[0].weight

    print(graph.depth_first(node_a))
