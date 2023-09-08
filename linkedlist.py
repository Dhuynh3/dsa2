# Example of a Singly Linked List Node
class ListNode: 
    def __init__(self, value, id, priority=0):
        self.value = value
        self.priority = priority
        self.id = id
        self.next = None
# Singly Linked List Implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # You can insert any node class as long as it has a next attribute
    def append_node(self, new_list_node):
        # If head is null, we're inserting the first node in the list.
        if self.head == None:
            # First node will be the the head and tail
            self.head = new_list_node
            self.tail = new_list_node
        else:
        # Not first node inserted in the list
            # Take the curent tail's next and point it to the new node
            self.tail.next = new_list_node
            # Set the tail to be our new node
            self.tail = new_list_node
        return
    # Checks to see if we have that node in our list already
    def has_value(self, id):
        current_node = self.head
        while current_node:
            if current_node.id == id:
                return True
            current_node = current_node.next
        return False
    # Append a node without duplicates
    def append_node_without_duplicates(self, new_list_node):
        if not self.has_value(new_list_node.id):
            self.append_node(new_list_node)
        else:
            print(f"Value {new_list_node} is already present in the list.")
    # Get the size of the linked list
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    # Traverse the linked list and print information
    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.id))
            current_node = current_node.next
        print(" -> ".join(nodes))