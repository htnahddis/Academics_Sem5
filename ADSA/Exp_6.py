class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point  # k-dimensional point
        self.left = left
        self.right = right

class KDTree:
    def __init__(self, k=2):
        """
        Initialize KD-Tree
        k: number of dimensions (default 2 for 2D points)
        """
        self.root = None
        self.k = k
    
    def insert(self, point):
        """Insert a point into the KD-Tree"""
        if len(point) != self.k:
            raise ValueError(f"Point must have {self.k} dimensions")
        
        print(f"Inserting point: {point}")
        self.root = self._insert_recursive(self.root, point, depth=0)
        print(f"  Successfully inserted\n")
    
    def _insert_recursive(self, node, point, depth):
        """
        Recursive insertion
        - depth determines which dimension to compare (depth % k)
        - Go left if point[cd] < node.point[cd], else right
        """
        # Base case: found empty position
        if node is None:
            return Node(point)
        
        # Calculate current dimension
        cd = depth % self.k
        
        print(f"  Depth {depth}, comparing dimension {cd}: {point[cd]} vs {node.point[cd]}")
        
        # Compare and recurse
        if point[cd] < node.point[cd]:
            print(f"    Going LEFT (smaller)")
            node.left = self._insert_recursive(node.left, point, depth + 1)
        else:
            print(f"    Going RIGHT (greater or equal)")
            node.right = self._insert_recursive(node.right, point, depth + 1)
        
        return node
    
    def delete(self, point):
        """Delete a point from the KD-Tree"""
        if len(point) != self.k:
            raise ValueError(f"Point must have {self.k} dimensions")
        
        print(f"Deleting point: {point}")
        self.root = self._delete_recursive(self.root, point, depth=0)
        print(f"  Successfully deleted\n")
    
    def _delete_recursive(self, node, point, depth):
        """
        Recursive deletion
        Three cases:
        1. Node is leaf: simply remove it
        2. Node has right subtree: replace with minimum of right subtree
        3. Node has only left subtree: replace with minimum of left subtree,
           then make left subtree the right subtree
        """
        # Base case: node not found
        if node is None:
            print(f"  Point not found!")
            return None
        
        # Calculate current dimension
        cd = depth % self.k
        
        # If point matches current node
        if node.point == point:
            print(f"  Found point at depth {depth}")
            
            # Case 1: Node has right child
            if node.right is not None:
                print(f"    Case 1: Has right subtree")
                # Find minimum in right subtree for current dimension
                min_node = self._find_min(node.right, cd, depth + 1)
                print(f"    Replacing with minimum from right: {min_node.point}")
                node.point = min_node.point
                node.right = self._delete_recursive(node.right, min_node.point, depth + 1)
            
            # Case 2: Node has only left child
            elif node.left is not None:
                print(f"    Case 2: Has only left subtree")
                # Find minimum in left subtree for current dimension
                min_node = self._find_min(node.left, cd, depth + 1)
                print(f"    Replacing with minimum from left: {min_node.point}")
                node.point = min_node.point
                # Move left subtree to right (important!)
                node.right = self._delete_recursive(node.left, min_node.point, depth + 1)
                node.left = None
            
            # Case 3: Leaf node
            else:
                print(f"    Case 3: Leaf node, removing")
                return None
            
            return node
        
        # Point doesn't match, recurse down the tree
        if point[cd] < node.point[cd]:
            print(f"  Depth {depth}, going LEFT")
            node.left = self._delete_recursive(node.left, point, depth + 1)
        else:
            print(f"  Depth {depth}, going RIGHT")
            node.right = self._delete_recursive(node.right, point, depth + 1)
        
        return node
    
    def _find_min(self, node, dim, depth):
        """
        Find node with minimum value in given dimension
        dim: dimension to minimize
        depth: current depth in tree
        """
        if node is None:
            return None
        
        cd = depth % self.k
        
        # If current dimension is same as target dimension
        if cd == dim:
            # Minimum must be in left subtree or current node
            if node.left is None:
                return node
            return self._find_min(node.left, dim, depth + 1)
        
        # Need to check both subtrees
        left_min = self._find_min(node.left, dim, depth + 1)
        right_min = self._find_min(node.right, dim, depth + 1)
        
        # Return minimum among node, left_min, right_min
        return self._min_node(node, left_min, right_min, dim)
    
    def _min_node(self, x, y, z, dim):
        """Return node with minimum value in given dimension"""
        res = x
        
        if y is not None and y.point[dim] < res.point[dim]:
            res = y
        if z is not None and z.point[dim] < res.point[dim]:
            res = z
        
        return res
    
    def search(self, point):
        """Search for a point in the KD-Tree"""
        print(f"Searching for point: {point}")
        result = self._search_recursive(self.root, point, depth=0)
        if result:
            print(f"  Point FOUND!\n")
        else:
            print(f"  Point NOT FOUND\n")
        return result
    
    def _search_recursive(self, node, point, depth):
        """Recursive search"""
        if node is None:
            return False
        
        if node.point == point:
            return True
        
        cd = depth % self.k
        
        print(f"  Depth {depth}, comparing dimension {cd}")
        
        if point[cd] < node.point[cd]:
            print(f"    Going LEFT")
            return self._search_recursive(node.left, point, depth + 1)
        else:
            print(f"    Going RIGHT")
            return self._search_recursive(node.right, point, depth + 1)
    
    def inorder_traversal(self):
        """Print all points in inorder"""
        print("Inorder Traversal:")
        result = []
        self._inorder_recursive(self.root, result)
        print("  Points:", result)
        print()
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.point)
            self._inorder_recursive(node.right, result)
    
    def range_search(self, lower_bound, upper_bound):
        """
        Find all points within a rectangular range
        lower_bound: [min_x, min_y, ...]
        upper_bound: [max_x, max_y, ...]
        """
        print(f"Range Search: {lower_bound} to {upper_bound}")
        result = []
        self._range_search_recursive(self.root, lower_bound, upper_bound, result, depth=0)
        print(f"  Found {len(result)} points: {result}\n")
        return result
    
    def _range_search_recursive(self, node, lower_bound, upper_bound, result, depth):
        """Recursive range search"""
        if node is None:
            return
        
        # Check if current point is in range
        in_range = all(lower_bound[i] <= node.point[i] <= upper_bound[i] 
                      for i in range(self.k))
        
        if in_range:
            result.append(node.point)
        
        cd = depth % self.k
        
        # Recursively search left subtree if it could contain points in range
        if lower_bound[cd] <= node.point[cd]:
            self._range_search_recursive(node.left, lower_bound, upper_bound, result, depth + 1)
        
        # Recursively search right subtree if it could contain points in range
        if upper_bound[cd] >= node.point[cd]:
            self._range_search_recursive(node.right, lower_bound, upper_bound, result, depth + 1)
    
    def print_tree(self):
        """Print tree structure"""
        print("Tree Structure:")
        self._print_tree_recursive(self.root, "", True, 0)
        print()
    
    def _print_tree_recursive(self, node, prefix, is_tail, depth):
        """Helper to print tree structure"""
        if node is not None:
            cd = depth % self.k
            # Use ASCII characters instead of Unicode for better compatibility
            connector = "+-- " if is_tail else "|-- "
            print(prefix + connector + f"{node.point} [dim={cd}]")
            
            children = []
            if node.left is not None:
                children.append((node.left, False))
            if node.right is not None:
                children.append((node.right, True))
            
            for i, (child, is_last) in enumerate(children):
                extension = "    " if is_tail else "|   "
                self._print_tree_recursive(child, prefix + extension, 
                                          is_last, depth + 1)


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 70)
    print("KD-TREE IMPLEMENTATION - INSERTION AND DELETION")
    print("=" * 70)
    print()
    
    # Create 2D KD-Tree
    kdtree = KDTree(k=2)
    
    # Example 1: Insertion
    print("EXAMPLE 1: INSERTION")
    print("-" * 70)
    points = [(30, 40), (5, 25), (70, 70), (10, 12), (50, 30), (35, 45)]
    
    for point in points:
        kdtree.insert(point)
    
    print("Tree after all insertions:")
    kdtree.print_tree()
    
    # Show inorder traversal
    kdtree.inorder_traversal()
    
    # Example 2: Search
    print("\nEXAMPLE 2: SEARCH")
    print("-" * 70)
    kdtree.search((50, 30))  # Should find
    kdtree.search((100, 100))  # Should not find
    
    # Example 3: Range Search
    print("\nEXAMPLE 3: RANGE SEARCH")
    print("-" * 70)
    kdtree.range_search([0, 0], [40, 50])
    
    # Example 4: Deletion
    print("\nEXAMPLE 4: DELETION")
    print("-" * 70)
    
    print("Deleting leaf node (10, 12):")
    print("-" * 70)
    kdtree.delete((10, 12))
    kdtree.print_tree()
    
    print("Deleting node with children (5, 25):")
    print("-" * 70)
    kdtree.delete((5, 25))
    kdtree.print_tree()
    
    print("Deleting root node (30, 40):")
    print("-" * 70)
    kdtree.delete((30, 40))
    kdtree.print_tree()
    
    print("Final tree traversal:")
    kdtree.inorder_traversal()
    
    # Example 5: 3D KD-Tree
    print("\nEXAMPLE 5: 3D KD-TREE")
    print("-" * 70)
    kdtree_3d = KDTree(k=3)
    
    points_3d = [(3, 6, 1), (17, 15, 2), (13, 15, 3), (6, 12, 4), 
                 (9, 1, 5), (2, 7, 6), (10, 19, 7)]
    
    for point in points_3d:
        kdtree_3d.insert(point)
    
    print("3D Tree structure:")
    kdtree_3d.print_tree()
    
    print("3D Range search [0,0,0] to [10,10,5]:")
    kdtree_3d.range_search([0, 0, 0], [10, 10, 5])
    
    print("=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)