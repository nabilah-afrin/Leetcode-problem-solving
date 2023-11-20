grph = {1:[2,3],
 2:[1,3,4],
 3:[1,2],
 4:[2]}

def bfs(grph):
    visited = set()
    queue = [grph[0]]
    while queue:
        current_node = queue.pop(0) #every time the first will be visited
        # first node obv note visited
        visited.add(current_node)
        
        for neighbours in grph[current_node]:
            if neighbours not in visited:
                visited.add(neighbours) #add adds in last
                queue.append(neighbours)
    return visited
result = print(bfs(grph))              
        
        
            
        