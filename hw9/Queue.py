class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

class Queue:
    def __init__(self, max_size=-1):
        self.front = Stack()  # Stack that holds the front half of the elements
        self.back = Stack()   # Stack that holds the back half of the elements
        self.max_size = max_size
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.max_size != -1 and self.current_size == self.max_size

    def enqueue(self, new_elem):
        if self.is_full():
            print("Queue Overflow!")
            return
        self.back.push(new_elem)
        self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        if self.front.is_empty():
            while not self.back.is_empty():
                self.front.push(self.back.pop())
        self.current_size -= 1
        return self.front.pop()

    def __del__(self):
        del self.front
        del self.back

queue = Queue(5)  #size of 5 but six elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)  
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue()) 