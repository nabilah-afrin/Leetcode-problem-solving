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

# Graph Implementation

<img src = "https://s3.stackabuse.com/media/articles/graphs-in-python-representing-graphs-in-code-4.png" height = "250" width = "300">
3 types: `adjacency matrices, adjacency lists, and lists of edges.`

## List of edges
We know, each edge connects two nodes and may have a weight assigned to it.
Therefore, each edge is represented by a list in the following way: `[node1, node2, weight]`, where weight is an optional property (not required if you have an unweighted graph). As its name suggests, a list of edges stores a graph as a list of edges represented in the described way.
<img src = "https://s3.stackabuse.com/media/articles/graphs-in-python-representing-graphs-in-code-5.png" height = "400" width = "700">
```python
class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        
        # Different representations of a graph
        self.m_list_of_edges = []
	
    # Add edge to a graph
    def add_edge(self, node1, node2, weight=1):        
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])
        
        # If a graph is undirected, add the same edge,
        # but also in the opposite direction
        if not self.m_directed:
            self.m_list_of_edges.append([node1, node2, weight])

	# Print a graph representation
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])
graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()
```
```yaml
OUTPUT:
edge  1 :  [0, 0, 25]
edge  2 :  [0, 1, 5]
edge  3 :  [0, 2, 3]
edge  4 :  [1, 3, 1]
edge  5 :  [1, 4, 15]
edge  6 :  [4, 2, 7]
edge  7 :  [4, 3, 11]
```

