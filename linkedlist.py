# Singly Linked List Node
class ListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None
# Singly Linked List Implementation
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # You can insert any node class as long as it has a next attribute
    def insert_node(self, new_list_node):
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
    # Print the Linked List
    def display(self):
        nodes = []
        current_node = self.head
        # Traverse the list
        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.next
        print(" -> ".join(nodes))