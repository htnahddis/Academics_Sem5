class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 for Red, 0 for Black

class RBTreeDeletion:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insert(self, key):
        """Basic insertion for building the tree"""
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def delete(self, data):
        """Delete a node with given data"""
        node = self.search_tree(self.root, data)
        if node == self.NULL:
            print(f"Value {data} not found in tree")
            return
        self.delete_node(node)

    def delete_node(self, node):
        y = node
        y_original_color = y.color
        
        if node.left == self.NULL:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NULL:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        
        if y_original_color == 0:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotate_left(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rotate_right(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rotate_right(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.rotate_left(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 0

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def search_tree(self, node, key):
        if node == self.NULL or key == node.data:
            return node

        if key < node.data:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder_helper(self, node):
        if node != self.NULL:
            self.inorder_helper(node.left)
            print(f"{node.data}({'R' if node.color == 1 else 'B'})", end=" ")
            self.inorder_helper(node.right)

    def print_tree(self):
        self.inorder_helper(self.root)
        print()


# Example usage
if __name__ == "__main__":
    rbt = RBTreeDeletion()
    
    # Build initial tree
    values = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    print("Building tree with values:", values)
    for val in values:
        rbt.insert(val)
    
    print("Initial tree:", end=" ")
    rbt.print_tree()
    
    # Delete nodes
    delete_values = [18, 11, 3, 10]
    for val in delete_values:
        print(f"\nDeleting {val}:", end=" ")
        rbt.delete(val)
        rbt.print_tree()
    
    print("\nFinal tree:", end=" ")
    rbt.print_tree()