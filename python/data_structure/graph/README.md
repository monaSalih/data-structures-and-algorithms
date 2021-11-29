# Graphs
<!-- Short summary or background information -->
write function for pargraph class
## Challenge
<!-- Description of the challenge -->
* breadth first
Arguments: Node
Returns:  A collection of nodes in the order they were visited.



## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
time:O(logn)
space:O(n)

## API
<!-- Description of each method publicly available in your Graph -->
```
class Graph:
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
        neighbor =  edge.vertex

        if neighbors not in visited:
            visited.add(neighbor)
            queue.enqueue(neighbors)

```
