# each edge connects two nodes and may have a weight assigned to it. 
# Therefore, each edge is represented by a list in the following way: [node1, node2, weight], 
# where weight is an optional property (not required if you have an unweighted graph). 
# As its name suggests, a list of edges stores a graph as a list of edges represented in the described way.

class EdgeListGraph(Graph):
      def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = []
        # Define the type of a graph
        self.m_directed = directed

        # A representation of a graph
        # i.e. list of edges
        self.m_graph = []

        # For Bovurka's algorithm
        self.m_components = {}
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
