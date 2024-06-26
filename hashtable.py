from linkedlist import SinglyLinkedList


# Chaining Hash Table with Linked List Implementation
class HashTable:
    # O(N)
    def __init__(self, size=16):
        self.buckets = []
        self.size = size
        for i in range(size):
            self.buckets.append(SinglyLinkedList())

    # O(1)
    def hash_function(self, key):
        return int(key) % self.size

    # O(1)
    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        self.buckets[bucket_index].append_node(value)
        return

    # O(1)
    def search(self, key):
        bucket_index = self.hash_function(key)
        return self.buckets[bucket_index]

    # Print the Hash Table
    def display(self):
        index = 0
        for bucket in self.buckets:
            print(f"[{index}] :")
            bucket.display()
            index += 1
