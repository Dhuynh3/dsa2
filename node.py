# Nodes represent individual hubs
class Node:
    # Required for each node
    def __init__(self, node_id, name, address):
        # Attributes needed for 2D Distance Matrix and pretty prints
        self.node_id = node_id
        self.name = name
        self.address = address
        # Dijkstra's Information
        self.previous_node = None
        self.shortest_distance_from_selected_node = float('inf')
    # Getters
    def get_node_id(self):
        return self.node_id
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_previous_node(self):
        return self.previous_node
    def get_shortest_distance(self):
        return self.shortest_distance_from_selected_node
    # Setters
    def set_node_id(self, new_node_id):
        self.node_id = new_node_id
    def set_name(self, new_name):
        self.name = new_name
    def set_address(self, new_address):
        self.address = new_address
    def set_previous_node(self, node):
        self.previous_node = node
    def set_shortest_distance(self, new_distance):
        self.shortest_distance_from_selected_node = new_distance
    # Pretty Prints
    def display(self):
        return f"Node {self.node_id} | Name : {self.name} | Address: {self.address}"