from datetime import datetime

# Example of a Singly Linked List Node
class ListNode: 
    # value : any object
    # id : int
    # priority : int
    def __init__(self, value, id, time=datetime.strptime("8:00 AM", "%I:%M %p"), next=None):
        self.value = value
        self.time = time
        self.id = int(id)
        # Needed to transverse the list
        self.next = next
    def snapshot(self):
        return ListNode(self.value, self.id, self.time)
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
            # print(f"Value {new_list_node} is already present in the list.")
            return
    # Taken from pirority queue implementation
    def dequeue(self):
        # If empty list return none
        if self.head == None:
            return None
        # Store the current head
        removed_node = self.head
        # Make the next the current head
        self.head = self.head.next
        # Returned the removed head
        return removed_node
    # Get the size of the linked list
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    # Make copy of Linked List
    def copy(self):
        # Create the new list
        copied_list = SinglyLinkedList()
        # Start at the head
        current_node = self.head
        while current_node:
            # Append a copied node
            copied_list.append_node(current_node.snapshot())
            # Move to the next node
            current_node = current_node.next
        # Return a reference to the copied list
        return copied_list
    # Traverse the linked list and print information
    def display(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.id))
            current_node = current_node.next
        print(" -> ".join(nodes))