# each edge connects two nodes and may have a weight assigned to it. 
# Therefore, each edge is represented by a list in the following way: [node1, node2, weight], 
# where weight is an optional property (not required if you have an unweighted graph). 
# As its name suggests, a list of edges stores a graph as a list of edges represented in the described way.

class EdgeListGraph(Graph):
     #constructor: total nodes, edge list, directed or undirected
	def __init__(self, total_nodes, edge_list, directed = True):
		self.nodes = total_nodes
		self.edges = [] #define the edge list
		self.directed = directed

	#create a method to add edge with two nodes
	def add_edge(node1, node2, wight=1):
		#create edge with directed
		self.edges.append([node1,node2,wight])

		#create edge undirected, but in opposite direction
		if not self.directed:
			self.edge.append([node1,node2,wight])

	#show the graph as edge list
	def print__edge_list(self):
		num_of_edges = len(self.edge_list)
		for i in range(num_of_edges):
			print(f"Edge {i+1} has {self.edge_list[i])"
graph = EdgeListGraph(5)
graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_edge_list()
