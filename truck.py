from hashtable import HashTable
from linkedlist import ListNode
from datamanager import DataManager
from datetime import datetime, timedelta
from linkedlist import SinglyLinkedList

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
        self.node_route = SinglyLinkedList()

    def get_time_key(self):
        return int(self.time_count.strftime("%H:%M").replace(":", "")) * 0.6

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
                        package.set_status("En route, time : " + self.time_count.strftime("%I:%M %p") + "| To Hub : " + package.get_address())
                        self.current_packages.append(package)
                        # When loading any package onto the truck, log the current package status in our hash table
                        self.package_records.insert(package.get_package_id(), ListNode(package.snapshot(),package.get_package_id()))
        # We have loaded the packages based on a given ID, now make a list of nodes we have to visit based on package address
        # For each package that is loaded.
        for package in self.current_packages:
            # Check against each node's address.
            for node in self.nodes_list:
                # If the package is meant for the node, add it to our node route.
                if package.get_address() == node.get_address():
                    self.node_route.append_node_without_duplicates(ListNode(node, node.get_node_id()))
    

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
        visited_nodes = SinglyLinkedList()
        unvisited_nodes = SinglyLinkedList()

    # Check if we have a package to deliver at the current node
    def deliver_package(self):
        return
    def get_package_records(self):
        return self.package_records
    def get_truck_id(self):
        return self.truck_id
    # Display Truck Information
    def display(self):
        return