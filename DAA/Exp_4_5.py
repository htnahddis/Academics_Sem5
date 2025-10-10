class Color:
    RED = "RED"
    BLACK = "BLACK"


class Node:
    def __init__(self, data=None, color=Color.RED, left=None, right=None, parent=None):
        self.data = data
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(color=Color.BLACK)
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
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

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
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

    def fix_insert(self, k):
        while k != self.root and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right  # Uncle
                if u.color == Color.RED:
                    k.parent.color = Color.BLACK
                    u.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left  # Uncle
                if u.color == Color.RED:
                    k.parent.color = Color.BLACK
                    u.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.left_rotate(k.parent.parent)
        self.root.color = Color.BLACK

    def insert(self, data):
        new_node = Node(data=data, color=Color.RED, left=self.NIL, right=self.NIL)
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y is None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:
            new_node.color = Color.BLACK
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def inorder_helper(self, node):
        if node != self.NIL:
            self.inorder_helper(node.left)
            print(f"{node.data}{'R' if node.color == Color.RED else 'B'}", end=" ")
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)
        print()

    def print_root(self):
        if self.root != self.NIL:
            print(f"Root node: {self.root.data}{'R' if self.root.color == Color.RED else 'B'}")
        else:
            print("Tree is empty.")


# Example usage
if __name__ == "__main__":
    tree = RedBlackTree()
    values = [10, 20, 30, 40, 1, 23, 54, 17]

    for v in values:
        tree.insert(v)

    print("Inorder traversal (value + color):")
    tree.inorder()

    tree.print_root()
