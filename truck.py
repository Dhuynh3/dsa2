from hashtable import HashTable
from linkedlist import ListNode
from datamanager import DataManager
from datetime import datetime, timedelta
from linkedlist import SinglyLinkedList

# Our delivery truck
class Truck(DataManager):
    def __init__(self, truck_id, start_time, capacity=16):
        super().__init__()
        self.truck_id = truck_id
        self.start_time = start_time
        self.time_count = datetime.strptime(start_time, "%I:%M %p")
        self.capacity = capacity
        self.speed = 18
        self.current_node = self.nodes_list[0]
        self.package_records = HashTable(len(self.packages_list))
        self.miles_traveled = 0
        self.current_packages = []
        self.node_route = []
        self.shortest_path = SinglyLinkedList()

    # Load the packages onto the truck then generate a must visit node route.
    def load_packages_by_id(self, list_of_package_ids):
        # For each of the package ID we want to load.
        for id in list_of_package_ids:
            # Check to see if the ID actually exists in the total package list.
            for package in self.packages_list:
                # We found the package ID in the list.
                if int(id) == int(package.get_package_id()):
                    # Check if the truck has enough space.
                    if len(self.current_packages) < self.capacity:
                        package.set_status(
                            "En route, time : "
                            + self.time_count.strftime("%I:%M %p")
                            + "| To Hub : "
                            + package.get_address()
                        )
                        self.current_packages.append(package)
                        # When loading any package onto the truck, log the current package status in our hash table
                        self.package_records.insert(
                            package.get_package_id(),
                            ListNode(package.snapshot(), int(package.get_package_id()), self.time_count),
                        )
                    else:
                        print(
                            f"Truck {self.truck_id} : Full not loading package : "
                            + package.get_package_id()
                        )
        # We have loaded the packages based on a given ID, now make a list of nodes we have to visit based on package address
        # For each package that is loaded.
        for package in self.current_packages:
            # Check against each node's address.
            for node in self.nodes_list:
                # If the package is meant for the node, add it to our node route.
                if package.get_address() == node.get_address():
                    # Multiple packages may go to the same node, don't add duplicates
                    if node not in self.node_route:
                        # Add the node to the route
                        self.node_route.append(node)
                    

    # Given a start node and a list of nodes to visit, dijkstra's algorithm will return a list of visited nodes
    # With all the previous vertex, and the shortest distance from the start node
    def dijkstra(self, start_node, nodes_list):
        # Initially each node in our node list should have their distance set infinte from the start node
        # They should also not have any previous nodes yet
        for nodes in nodes_list:
            nodes.set_shortest_distance(float("inf"))
            nodes.set_previous_node(None)
        # Shortest distance from start node to itself is 0 with no previous nodes
        start_node.set_shortest_distance(0.0)
        start_node.set_previous_node(None)
        # We need to keep track of visited and unvisited nodes
        visited_nodes = []
        # Make a copy of the node's list so we don't modify the reference and also include the start node
        unvisited_nodes = list(nodes_list)
        unvisited_nodes.append(start_node)
        # Vist every unvisited nodes
        while unvisited_nodes:
            # Find the node with the smallest known distance from the start node
            small_index = 0
            for i in range(len(unvisited_nodes)):
                if (unvisited_nodes[i].get_shortest_distance() < unvisited_nodes[small_index].get_shortest_distance()):
                    small_index = i

            # Select that node and remove it from the list
            currently_selected_node = unvisited_nodes.pop(small_index)
            # Mark it as visited
            visited_nodes.append(currently_selected_node)
            # We are checking every unvisited node because all nodes are connected
            for node in unvisited_nodes:
                calculated_distance = (
                    currently_selected_node.get_shortest_distance()
                    + self.get_distance_between_nodes(
                        node.get_id(), currently_selected_node.get_id()
                    )
                )
                if calculated_distance < nodes.get_shortest_distance():
                    nodes.set_shortest_distance(calculated_distance)
                    nodes.set_previous_node(currently_selected_node)
        return visited_nodes

    # Greedy part of Dijkstra, here's how it works
    # We start at a given node with a given list of nodes to visit
    # A list is returned with the shortest path to that given node
    # Go to that node and repeat the process
    def generate_shortest_path(self, start_node, end_node):
        # Start at the given start node
        self.shortest_path.append_node(start_node)
        while self.node_route:
            visited_nodes = self.dijkstra(start_node, self.node_route)

            for node in visited_nodes:
                if node.get_previous_node() == None:
                    visited_nodes.remove(node)

            min_node = min(visited_nodes, key=lambda node: node.shortest_distance_from_selected_node,)

            self.shortest_path.append_node(min_node)
            self.node_route.remove(min_node)
            start_node = min_node
        # End with the given end node
        self.shortest_path.append_node(end_node)

    # The truck will generate a path and travel on it to deliver it's packages
    def start_delivery(self, start_node, end_node):
        # This is a linked list esentally turned into a priority queue
        self.generate_shortest_path(start_node, end_node)

        return
    # Check to see if we have a package to deliver at the truck's current node
    def deliver_package(self):
        # For every package in our truck
        for package in self.current_packages:
            # Each time we hit a node and deliver, update the status of packages for the snapshot
            package.set_status("En route, time : " + self.time_count.strftime("%I:%M %p") + " To Address, " + package.get_package_address())
            # Is this package destined for this node?
            if package.get_address() == self.current_node.get_address():
                # Set it as delivered
                package.set_status("Delivered, time : " + self.time_count.strftime("%I:%M %p") + " To Address, " + self.current_location.get_name())
                # Remove the package from our current package list
                self.current_packages.remove(package)
            # Snapshot the status of packages
            self.package_records.insert(package.get_package_id(), ListNode(package.snapshot(), int(package.get_package_id()), self.time_count))
    # Return the hash table of package records
    def get_package_records(self):
        return self.package_records
    # Get the truck's ID
    def get_truck_id(self):
        return self.truck_id
    # Display Truck Information
    def display(self):
        return
    # Internally display the hashtable's package records
    def display_package_record(self):
        return