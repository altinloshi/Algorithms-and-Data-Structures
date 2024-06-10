class Color:
    RED = 0
    BLACK = 1

class Node:
    def __init__(self, data):
        self.data = data
        self.color = Color.RED  # New nodes are always RED
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nil = None  # Nil node, equivalent to nullptr in C++

    def rotate_left(self, rotate):
        pivot = Node(rotate.right.data)
        pivot.left = rotate.right.left
        pivot.right = rotate.right.right

        rotate.right = pivot.left

        if pivot.left != self.nil:
            pivot.left.parent = rotate
        pivot.parent = rotate.parent

        if rotate.parent == self.nil:
            self.root = pivot
        elif rotate == rotate.parent.left:
            rotate.parent.left = pivot
        else:
            rotate.parent.right = pivot

        rotate.parent = pivot
        pivot.left = rotate

    def rotate_right(self, rotate):
        pivot = Node(rotate.left.data)
        pivot.left = rotate.left.left
        pivot.right = rotate.left.right

        rotate.left = pivot.right

        if pivot.right != self.nil:
            pivot.right.parent = rotate
        pivot.parent = rotate.parent

        if rotate.parent == self.nil:
            self.root = pivot
        elif rotate == rotate.parent.right:
            rotate.parent.right = pivot
        else:
            rotate.parent.left = pivot

        pivot.right = rotate
        rotate.parent = pivot

    def insertRB_fixup(self, new_node):
        if new_node == self.root:
            new_node.color = Color.BLACK
            return

        while new_node.parent.color == Color.RED:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                
                if uncle.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                    break
                elif new_node == new_node.parent.right:
                    new_node = new_node.parent
                    self.rotate_left(new_node)

                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.rotate_right(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left

                if uncle.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                    break
                elif new_node == new_node.parent.left:
                    new_node = new_node.parent
                    self.rotate_right(new_node)

                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self.rotate_left(new_node.parent.parent)

        self.root.color = Color.BLACK

    def insertRB(self, new_data):
        new_node = Node(new_data)
        leaf = self.nil
        iterator = self.root

        while iterator != self.nil:
            leaf = iterator
            if new_node.data < iterator.data:
                iterator = iterator.left
            else:
                iterator = iterator.right

        new_node.parent = leaf
        if leaf == self.nil:
            self.root = new_node
        elif new_node.data < leaf.data:
            leaf.left = new_node
        else:
            leaf.right = new_node

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = Color.RED
        self.insertRB_fixup(new_node)

    def transplantRB(self, node, subtree):
        if node.parent == self.nil:
            self.root = subtree
        elif node == node.parent.left:
            node.parent.left = subtree
        else:
            node.parent.right = subtree

        if subtree != self.nil:
            subtree.parent = node.parent

    def deleteRB_fixup(self, node):
        while node != self.root and node.color == Color.BLACK:
            if node == node.parent.left:
                sibling = node.parent.right

                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_left(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == Color.BLACK and sibling.right.color == Color.BLACK:
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    if sibling.right.color == Color.BLACK:
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.rotate_right(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left

                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_right(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == Color.BLACK and sibling.left.color == Color.BLACK:
                    sibling.color = Color.RED
                    node = node.parent
                else:
                    if sibling.left.color == Color.BLACK:
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.rotate_left(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self.rotate_right(node.parent)
                    node = self.root
        node.color = Color.BLACK

    def deleteRB(self, delete_node):
        to_delete = delete_node
        child = None
        original_color = to_delete.color

        if delete_node.left == self.nil:
            child = delete_node.right
            self.transplantRB(delete_node, delete_node.right)
        elif delete_node.right == self.nil:
            child = delete_node.left
            self.transplantRB(delete_node, delete_node.left)
        else:
            to_delete = self.getMinimum(delete_node.right)
            original_color = to_delete.color
            child = to_delete.right

            if to_delete.parent == delete_node:
                child.parent = to_delete
            else:
                self.transplantRB(to_delete, to_delete.right)
                to_delete.right = delete_node.right
                to_delete.right.parent = to_delete

            self.transplantRB(delete_node, to_delete)
            to_delete.left = delete_node.left
            to_delete.left.parent = to_delete
            to_delete.color = delete_node.color

        if original_color == Color.BLACK:
            self.deleteRB_fixup(child)
