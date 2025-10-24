class Graph:
    """Graph implementation using an adjacency list."""

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        """Add an undirected edge between vertices u and v."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        """
        Perform Breadth-First Search (BFS) starting from 'start' vertex.
        Returns a list of vertices in BFS order.
        """
        visited = set()
        queue = []
        order = []

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """
        Perform Depth-First Search (DFS) starting from 'start' vertex.
        Returns a list of vertices in DFS order.
        """
        visited = set()
        order = []

        def _dfs_recursive(vertex):
            visited.add(vertex)
            order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start)
        return order

# Example usage and test
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Adjacency List:", g.adj_list)
    print("BFS from 1:", g.bfs(1))
    print("DFS from 1:", g.dfs(1))