from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = []
        queue = []

        queue.append(start)
        visited.append(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

if __name__ == "__main__":
    g = Graph()
    n = int(input("Enter number of nodes: "))
    m = int(input("Enter number of edges: "))
    print("Enter the edges: ")
    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a, b)
    start = int(input("Enter the starting node for BFS: "))
    g.bfs(start)
