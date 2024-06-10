class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

def bst2l(head):
    if head is None:
        return None

    middle = head
    left_side = None
    right_side = None

    iterator = head
    while iterator and iterator.next:
        left_side = middle
        middle = middle.next
        iterator = iterator.next.next

    right_side = middle.next if middle else None
    root = TreeNode(middle.elem) if middle else None

    if left_side:
        left_side.next = None
        if root:
            root.left = bst2l(head)

    if root:
        root.right = bst2l(right_side)

    return root

if __name__ == "__main__":
    # Creating a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Converting the linked list to a binary search tree
    root = bst2l(head)

    # Displaying the elements of the binary search tree (in-order traversal)
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            print(node.elem, end=" ")
            in_order_traversal(node.right)

    print("In-order traversal of the binary search tree:")
    in_order_traversal(root)

#The recursion formula would be: T(n) = 2T(n/2) + n where by using the master 
#theorem we derive the time complexity of O(n*logn)