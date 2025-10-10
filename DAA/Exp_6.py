class Node:
    def __init__(self, point, depth=0, left=None, right=None):
        self.point = point
        self.depth = depth
        self.left = left
        self.right = right


class KDTree:
    def __init__(self, k):
        self.root = None
        self.k = k  # Number of dimensions

    def insert(self, root, point, depth=0):
        if root is None:
            return Node(point, depth)

        axis = depth % self.k
        if point[axis] < root.point[axis]:
            root.left = self.insert(root.left, point, depth + 1)
        else:
            root.right = self.insert(root.right, point, depth + 1)
        return root

    def insert_point(self, point):
        self.root = self.insert(self.root, point)

    def find_min(self, root, d, depth=0):
        if root is None:
            return None

        axis = depth % self.k

        if axis == d:
            if root.left is None:
                return root
            return self.find_min(root.left, d, depth + 1)

        left_min = self.find_min(root.left, d, depth + 1)
        right_min = self.find_min(root.right, d, depth + 1)

        min_node = root
        for node in [left_min, right_min]:
            if node and node.point[d] < min_node.point[d]:
                min_node = node
        return min_node

    def delete(self, root, point, depth=0):
        if root is None:
            return None

        axis = depth % self.k

        if root.point == point:
            if root.right:
                min_node = self.find_min(root.right, axis, depth + 1)
                root.point = min_node.point
                root.right = self.delete(root.right, min_node.point, depth + 1)
            elif root.left:
                min_node = self.find_min(root.left, axis, depth + 1)
                root.point = min_node.point
                root.right = self.delete(root.left, min_node.point, depth + 1)
                root.left = None
            else:
                return None
            return root

        if point[axis] < root.point[axis]:
            root.left = self.delete(root.left, point, depth + 1)
        else:
            root.right = self.delete(root.right, point, depth + 1)

        return root

    def delete_point(self, point):
        self.root = self.delete(self.root, point)

    def preorder(self, root):
        if root:
            print(root.point)
            self.preorder(root.left)
            self.preorder(root.right)

tree = KDTree(k=2)
points = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
for p in points:
    tree.insert_point(p)

print("Preorder traversal before deletion:")
tree.preorder(tree.root)

tree.delete_point((13, 15))

print("\nPreorder traversal after deletion:")
tree.preorder(tree.root)
