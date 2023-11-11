Graphs are non-linear DS, that represent relationships; graphs consist of vertices (nodes) and edges; which are represented as __*G(V,E)*__ . vertices that are connected by an edge are said to be adjacent to each other. Some also refer to adjacent vertices as neighbors.
<div style="width: 200px;">
<img src = "https://media.geeksforgeeks.org/wp-content/uploads/20200630111809/graph18.jpg" width="300" >
<img src = "https://s3.stackabuse.com/media/articles/graphs-in-python-representing-graphs-in-code-1.png" width="300">
</div>

### Trees vs Graphs
trees can be considered as a type of graph. Both data structures consist of nodes connected to each other. while all trees are graphs, not all graphs are trees. Trees cannot have cycles, and all nodes must be connected.

A graph may have nodes that form a cycle; meaning, nodes that reference each other circularly. In other words, a cycle is a sequence of edges that starts and ends at the same vertex.

Another characteristic specific to trees is that __every node is connected to every other node__, even if the connections are indirect. However, it’s
possible for a graph to not be fully connected. Meaning a node might not be connected with any other nodes in a graph.
```python
# Base class for graph representation
class Graph:
    def __init__(self, num_of_nodes):
        return

    def __str__(self):
        return

    def add_edge(self, node1, node2, weight):
        return
```
__Nodes__
```python
class Node:
    def __init__(self, name, id=-1):
        self.m_id = id
        self.m_name = str(name)

    def __str__(self):
        return "node " + self.m_name

    def __repr__(self):
        return "node " + self.m_name


    def set_id(self, id):
        self.m_id = id

    def get_id(self):
        return self.m_id

    def get_name(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)
```
