from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited.add(start)
        print(start, end=' ')
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter number of nodes: "))
    m = int(input("Enter number of edges: "))
    print("Enter the edges: ")
    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a, b)
    
    start = int(input("Enter the starting node for DFS: "))
    visited = set()
    g.dfs(start, visited)
