from datetime import datetime
# Example of a Singly Linked List Node
class ListNode: 
    # value : any object
    # id : int
    # priority : int
    def __init__(self, value, id, truck_id, time=datetime.strptime("8:00 AM", "%I:%M %p"), next=None):
        self.value = value
        self.time = time
        self.id = int(id)
        self.truck_id = truck_id
        # Needed to transverse the list
        self.next = next
    def snapshot(self):
        return ListNode(self.value, self.id, self.time, self.truck_id)
# Singly Linked List Implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def prepend_node(self, new_list_node):
        # If head is null, we're inserting the first node in the list.
        if self.head == None:
            # First node will be the the head and tail
            self.head = new_list_node
            self.tail = new_list_node
        else:
        # Not first node inserted in the list
            # Set new node's next as head
            new_list_node.next = self.head
            # Head is now new node
            self.head = new_list_node
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
    def is_empty(self):
        return True if self.head == None else False
    # Pirority queue implementation
    def dequeue(self):
        # If empty list return none
        if self.is_empty() == True:
            return None
        # Get the current head
        current_node = self.head
        # If it's not the tail
        if current_node != self.tail:
            self.head = self.head.next
        # Else it's the tail
        else:
            self.head = None
            self.tail = None
        return current_node
    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.head
    # Get the size of the linked list
    def size(self):
        count = 0
        current_node = self.head
        while current_node != self.tail:
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
            nodes.append(str(current_node.value.display()))
            current_node = current_node.next
        print("\n".join(nodes))