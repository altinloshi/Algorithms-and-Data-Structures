class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.maxSize = 16
        self.currentSize = 0
        self.arr = [None] * self.maxSize

    def hashCode(self, key):
        return key % self.maxSize

    def insertNode(self, key, value):
        index = self.hashCode(key)
        counter = 1

        while self.arr[index] is not None:
            if counter == self.maxSize:
                print("Hash Table is full!")
                return

            # Update value if key already exists
            if self.arr[index].key == key:
                self.arr[index].value = value
                return

            # Increment index and get new index
            index += 1
            index = self.hashCode(index)
            counter += 1

        print(index)
        self.arr[index] = Node(key, value)
        self.currentSize += 1

    def get(self, key):
        index = self.hashCode(key)
        counter = 1

        while self.arr[index] is not None:
            if counter == self.maxSize:
                break

            if self.arr[index].key == key:
                return self.arr[index].value

            index += 1
            index = self.hashCode(index)
            counter += 1

        print("Key does not exist!")
        return -1

    def isEmpty(self):
        return self.currentSize == 0
