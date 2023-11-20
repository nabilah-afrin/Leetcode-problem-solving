grph = {1:[2,3],
 2:[1,3,4],
 3:[1,2],
 4:[2]}

def dfs(graph, start_node):
    visited = set()
    visited.add(start_node)
    for neighbours in graph[start_node]:
        if neighbours not in visited:
            dfs(graph, neighbours)
        
    return visited  
        


print(dfs(grph, 1))
   
            
        