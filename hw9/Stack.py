class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Stack:
    def __init__(self, max_size=-1):
        self.top = None
        self.max_size = max_size
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def push(self, new_elem):
        if self.current_size == self.max_size:
            print("Stack Overflow!")
            return

        new_top = Node(new_elem)
        new_top.next = self.top
        self.top = new_top

        self.current_size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow!")

        deleted_elem = self.top.elem
        self.top = self.top.next

        self.current_size -= 1

        return deleted_elem

    def __whydel__(self):
        while self.top:
            temp = self.top
            self.top = self.top.next
            del temp

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # Output 3
    print(stack.pop())  # Output 2
    print(stack.pop())  # Output 1
