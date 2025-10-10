from collections import defaultdict

class FordFulkerson:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: defaultdict(int))
    
    def add_edge(self, u, v, capacity):
        """Add an edge with given capacity"""
        self.graph[u][v] = capacity
    
    def bfs(self, source, sink, parent):
        """BFS to find if there's a path from source to sink"""
        visited = set([source])
        queue = [source]
        
        while queue:
            u = queue.pop(0)
            
            for v in self.graph[u]:
                if v not in visited and self.graph[u][v] > 0:
                    visited.add(v)
                    queue.append(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(self, source, sink):
        """
        Returns the maximum flow from source to sink
        Uses BFS to find augmenting paths (Edmonds-Karp implementation)
        """
        parent = {}
        max_flow = 0
        paths = []
        
        print(f"\nFinding maximum flow from {source} to {sink}...")
        print("-" * 50)
        
        iteration = 1
        while self.bfs(source, sink, parent):
            # Find minimum residual capacity along the path
            path_flow = float('inf')
            s = sink
            path = []
            
            while s != source:
                path.append(s)
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            path.append(source)
            path.reverse()
            
            paths.append((path, path_flow))
            print(f"Iteration {iteration}:")
            print(f"  Augmenting path: {' -> '.join(map(str, path))}")
            print(f"  Path flow: {path_flow}")
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            
            max_flow += path_flow
            print(f"  Total flow so far: {max_flow}\n")
            parent = {}
            iteration += 1
        
        print("-" * 50)
        print(f"\nMaximum Flow: {max_flow}")
        print(f"\nAll augmenting paths:")
        for i, (path, flow) in enumerate(paths, 1):
            print(f"  Path {i}: {' -> '.join(map(str, path))} (flow: {flow})")
        
        return max_flow


# Example usage
if __name__ == "__main__":
    # Create a graph
    g = FordFulkerson(6)
    
    # Add edges (u, v, capacity)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)
    
    print("Graph Edges (source -> destination: capacity):")
    print("-" * 50)
    for u in g.graph:
        for v in g.graph[u]:
            if g.graph[u][v] > 0:
                print(f"  {u} -> {v}: {g.graph[u][v]}")
    
    source = 0
    sink = 5
    
    max_flow = g.ford_fulkerson(source, sink)
    
    print("\n" + "=" * 50)
    print(f"RESULT: Maximum flow from {source} to {sink} is {max_flow}")
    print("=" * 50)