from collections import deque

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph if it doesn't exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        # Add an edge between src and dest (undirected)
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  # For undirected graph

    def bfs(self, start):
        # Breadth-first search traversal from start vertex
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                queue.extend(n for n in self.adj_list[vertex] if n not in visited)
        return order

    def dfs(self, start):
        # Depth-first search traversal from start vertex
        visited = set()
        order = []

        def _dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def __repr__(self):
        # Return a string representation of the graph
        return f"Graph({self.adj_list})"

# Example usage
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
print(g)                  # Output: Graph({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']})
print("BFS:", g.bfs('A')) # Output: BFS: ['A', 'B', 'C', 'D', 'E']
print("DFS:", g.dfs('A')) # Output: DFS: ['A', 'B', 'D', 'C', 'E']
