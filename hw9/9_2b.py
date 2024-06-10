class Node:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None

def convert(root, prev, head):
    if root is None:
        return
    
    convert(root.left, prev, head)

    if prev[0] is None:
        head[0] = root
    else:
        prev[0].right = root

    prev[0] = root
    convert(root.right, prev, head)

def bst_to_list(root):
    if root is None:
        return None

    prev = [None]
    head = [None]
    convert(root, prev, head)

    return head[0]

def print_linked_list(linked_list_head):
    while linked_list_head:
        print(linked_list_head.elem, end=" ")
        linked_list_head = linked_list_head.right
    print()

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    linked_list_head = bst_to_list(root)
    print_linked_list(linked_list_head)
