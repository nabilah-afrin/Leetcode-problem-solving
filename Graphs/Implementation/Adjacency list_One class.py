class Graph:
  # constrcutor: vertics or node will be instances
  def __init__(self):
    self.nodes = {}

  def add_node(self, value):
    self.nodes[value] = [] #create a list as dictionary to store the adjacent nodes

  def edges(self,initial_node, final_node):
    #this will creeate the actual hashmap by adding elements
    self.nodes[initial_node].append(final_node)
    self.nodes[final_node].append(initial_node)
# Example Usage
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.edges('A', 'B')


"""class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = [] #list of nodes

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)"""
