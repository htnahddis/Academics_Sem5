class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    
    def add_edge(self, u, v):
        """Add an undirected edge"""
        self.edges.append((u, v))
    
    def vertex_cover_approx(self):
        """
        2-Approximation Algorithm for Vertex Cover
        
        Algorithm:
        1. Start with empty vertex cover
        2. While there are uncovered edges:
           - Pick an arbitrary edge (u, v)
           - Add both u and v to the cover
           - Remove all edges incident to u or v
        
        This gives at most 2 * OPT solution
        """
        # Create a copy of edges to work with
        remaining_edges = self.edges.copy()
        vertex_cover = set()
        covered_edges = []
        
        print("Starting Vertex Cover Approximation Algorithm")
        print("=" * 60)
        print(f"Total edges: {len(self.edges)}")
        print(f"Edges: {self.edges}\n")
        
        iteration = 1
        while remaining_edges:
            # Pick an arbitrary edge
            edge = remaining_edges[0]
            u, v = edge
            
            print(f"Iteration {iteration}:")
            print(f"  Selected edge: ({u}, {v})")
            
            # Add both vertices to cover
            vertex_cover.add(u)
            vertex_cover.add(v)
            print(f"  Added vertices {u} and {v} to cover")
            
            # Remove all edges covered by u or v
            edges_to_remove = []
            for e in remaining_edges:
                if u in e or v in e:
                    edges_to_remove.append(e)
                    covered_edges.append(e)
            
            for e in edges_to_remove:
                remaining_edges.remove(e)
            
            print(f"  Removed {len(edges_to_remove)} edges: {edges_to_remove}")
            print(f"  Remaining edges: {len(remaining_edges)}")
            print(f"  Current cover: {sorted(vertex_cover)}\n")
            
            iteration += 1
        
        print("=" * 60)
        print("Algorithm Complete!\n")
        print(f"Vertex Cover: {sorted(vertex_cover)}")
        print(f"Size of cover: {len(vertex_cover)}")
        print(f"\nAll edges covered: {covered_edges}")
        
        # Verify the cover
        self.verify_cover(vertex_cover)
        
        return vertex_cover
    
    def verify_cover(self, cover):
        """Verify that the cover is valid"""
        print("\nVerifying Vertex Cover...")
        print("-" * 60)
        
        all_covered = True
        for u, v in self.edges:
            if u in cover or v in cover:
                print(f"  Edge ({u}, {v}): ✓ Covered")
            else:
                print(f"  Edge ({u}, {v}): ✗ NOT Covered")
                all_covered = False
        
        if all_covered:
            print("\n✓ All edges are covered! Valid vertex cover.")
        else:
            print("\n✗ Some edges are not covered! Invalid cover.")
        
        return all_covered
    
    def greedy_vertex_cover(self):
        """
        Greedy approach: Select vertex with maximum degree repeatedly
        This is also an approximation but not guaranteed to be 2-approximation
        """
        remaining_edges = self.edges.copy()
        vertex_cover = set()
        
        print("\n\nGreedy Vertex Cover (for comparison)")
        print("=" * 60)
        
        iteration = 1
        while remaining_edges:
            # Count degree of each vertex
            degree = {}
            for u, v in remaining_edges:
                degree[u] = degree.get(u, 0) + 1
                degree[v] = degree.get(v, 0) + 1
            
            # Find vertex with maximum degree
            max_vertex = max(degree, key=degree.get)
            vertex_cover.add(max_vertex)
            
            print(f"Iteration {iteration}:")
            print(f"  Vertex degrees: {degree}")
            print(f"  Selected vertex: {max_vertex} (degree: {degree[max_vertex]})")
            
            # Remove all edges incident to max_vertex
            remaining_edges = [(u, v) for u, v in remaining_edges 
                              if u != max_vertex and v != max_vertex]
            
            print(f"  Remaining edges: {len(remaining_edges)}\n")
            iteration += 1
        
        print(f"Greedy Vertex Cover: {sorted(vertex_cover)}")
        print(f"Size: {len(vertex_cover)}")
        
        return vertex_cover


# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph(7)
    
    # Add edges
    edges_to_add = [
        (0, 1), (0, 2), (1, 2), (1, 3),
        (2, 3), (2, 4), (3, 5), (4, 5), (4, 6)
    ]
    
    for u, v in edges_to_add:
        g.add_edge(u, v)
    
    # Run 2-approximation algorithm
    cover = g.vertex_cover_approx()
    
    # Run greedy algorithm for comparison
    greedy_cover = g.greedy_vertex_cover()
    
    print("\n" + "=" * 60)
    print("COMPARISON:")
    print(f"2-Approximation cover size: {len(cover)}")
    print(f"Greedy cover size: {len(greedy_cover)}")
    print("=" * 60)