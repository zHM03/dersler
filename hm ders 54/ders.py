from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def dfs(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
                
    def bfs(self, v):
        visited = set()
        queue = [v]
        visited.add(v)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
print("DFS:")
g.dfs(2, set())
print("\nBFS:")
g.bfs(2)