import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class GrahamScan:
    def __init__(self, points):
        self.points = points
    
    def orientation(self, p, q, r):
        """
        Find orientation of ordered triplet (p, q, r)
        Returns:
            0 -> p, q and r are colinear
            1 -> Clockwise
            2 -> Counterclockwise
        
        Uses cross product: (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        
        if val == 0:
            return 0  # Colinear
        return 1 if val > 0 else 2  # Clockwise or Counterclockwise
    
    def distance_squared(self, p1, p2):
        """Calculate squared distance between two points"""
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
    
    def polar_angle(self, p0, p):
        """Calculate polar angle with respect to p0"""
        return math.atan2(p.y - p0.y, p.x - p0.x)
    
    def graham_scan(self):
        """
        Graham Scan Algorithm to find Convex Hull
        
        Steps:
        1. Find the bottom-most point (or left most in case of tie)
        2. Sort points by polar angle with respect to bottom-most point
        3. Process points and maintain a stack of hull points
        4. For each point, pop from stack while we make a right turn
        """
        n = len(self.points)
        
        if n < 3:
            print("Convex hull not possible with less than 3 points")
            return []
        
        print("Graham Scan Algorithm - Convex Hull")
        print("=" * 70)
        print(f"Input points: {self.points}\n")
        
        # Step 1: Find the bottom-most point (lowest y-coordinate)
        # If tie, choose leftmost point
        start_point = min(self.points, key=lambda p: (p.y, p.x))
        print(f"Step 1: Bottom-most point (starting point): {start_point}\n")
        
        # Step 2: Sort points by polar angle with respect to start_point
        # If two points have same angle, keep the farthest one
        def compare_points(p):
            angle = self.polar_angle(start_point, p)
            dist = self.distance_squared(start_point, p)
            return (angle, -dist)  # Negative dist to keep farthest point
        
        sorted_points = sorted(
            [p for p in self.points if p != start_point],
            key=compare_points
        )
        
        print("Step 2: Points sorted by polar angle:")
        for i, p in enumerate(sorted_points):
            angle = self.polar_angle(start_point, p)
            print(f"  {i+1}. {p} - angle: {math.degrees(angle):.2f}°")
        print()
        
        # Step 3: Process points using a stack
        stack = [start_point, sorted_points[0]]
        
        print("Step 3: Processing points...")
        print("-" * 70)
        print(f"Initial stack: {stack}\n")
        
        for i in range(1, len(sorted_points)):
            current_point = sorted_points[i]
            
            print(f"Processing point {current_point}:")
            
            # Pop while we make a non-left turn
            while len(stack) > 1:
                top = stack[-1]
                second_top = stack[-2]
                orientation = self.orientation(second_top, top, current_point)
                
                if orientation == 2:  # Counter-clockwise (left turn)
                    print(f"  {second_top} -> {top} -> {current_point}: Left turn (CCW)")
                    break
                else:
                    removed = stack.pop()
                    if orientation == 1:
                        print(f"  {second_top} -> {top} -> {current_point}: Right turn (CW) - Remove {removed}")
                    else:
                        print(f"  {second_top} -> {top} -> {current_point}: Collinear - Remove {removed}")
            
            stack.append(current_point)
            print(f"  Current hull: {stack}\n")
        
        print("=" * 70)
        print(f"\nConvex Hull (in order): {stack}")
        print(f"Number of points on hull: {len(stack)}")
        
        # Calculate perimeter
        perimeter = 0
        for i in range(len(stack)):
            p1 = stack[i]
            p2 = stack[(i + 1) % len(stack)]
            perimeter += math.sqrt(self.distance_squared(p1, p2))
        
        print(f"Perimeter of convex hull: {perimeter:.2f}")
        
        return stack
    
    def visualize_points(self):
        """Simple text-based visualization"""
        if not self.points:
            return
        
        # Find bounding box
        min_x = min(p.x for p in self.points)
        max_x = max(p.x for p in self.points)
        min_y = min(p.y for p in self.points)
        max_y = max(p.y for p in self.points)
        
        print("\nPoint Distribution:")
        print("-" * 50)
        print(f"X range: [{min_x}, {max_x}]")
        print(f"Y range: [{min_y}, {max_y}]")
        
        # Group points by approximate y-coordinate
        grid = {}
        scale = 5
        for p in self.points:
            y_bucket = round(p.y / scale) * scale
            if y_bucket not in grid:
                grid[y_bucket] = []
            grid[y_bucket].append(p)
        
        print("\nApproximate layout (Y-axis):")
        for y in sorted(grid.keys(), reverse=True):
            print(f"{y:5.0f} | {', '.join(str(p) for p in sorted(grid[y], key=lambda p: p.x))}")


# Example usage
if __name__ == "__main__":
    # Create sample points
    points = [
        Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
        Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3),
        Point(2, 1), Point(4, 2)
    ]
    
    gs = GrahamScan(points)
    
    # Show point distribution
    gs.visualize_points()
    
    print("\n" + "=" * 70 + "\n")
    
    # Find convex hull
    hull = gs.graham_scan()
    
    print("\n" + "=" * 70)
    print("CONVEX HULL VERTICES:")
    for i, point in enumerate(hull):
        print(f"  {i+1}. {point}")
    print("=" * 70)