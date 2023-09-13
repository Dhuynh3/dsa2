from hashtable import HashTable
from linkedlist import ListNode
from datamanager import DataManager
from datetime import datetime, timedelta
from linkedlist import SinglyLinkedList


"""Truck inherites DataManager which is responsible for feeding package, node and distance information to the truck"""
class Truck(DataManager):
    def __init__(self, truck_id, start_time, capacity=16, debug=False):
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
        self.debug = debug
#####################################################################################
    """ Get the list of nodes the truck must visit.
        This list is not optimized in order of travel.
    """
    def get_node_route_list(self):
        # Prepare the list
        truck_node_route = []
        # For every package on the truck
        for package in self.current_packages:
            # Compare it against every node
            for node in self.nodes_list:
                # If the address is the same, we know we have to deliver to this node
                if str(package.get_address()) == str(node.get_address()):
                    # Multiple packages may have the same node, we don't want duplicates
                    if node not in truck_node_route:   
                        # Append the node
                        truck_node_route.append(node)
        # Return the final list of nodes
        return truck_node_route                                                           
###########################################################################################
    def optimized_travel_path(self, start_node, end_node, list_of_node_route):
        optimized_travel_path = []
        begin_node = start_node
        optimized_travel_path.append(begin_node)
        while list_of_node_route:
            visited_node_list = self.dijkstra(start_node, list_of_node_route)
            for node in visited_node_list:
                if node.get_previous_node() == None:
                    visited_node_list.remove(node)
            min_node = min(visited_node_list, key=lambda node: node.shortest_distance_from_selected_node)
            optimized_travel_path.append(min_node)
            list_of_node_route.remove(min_node)
            start_node = min_node
        optimized_travel_path.append(end_node)
        return optimized_travel_path
###########################################################################################
    """ The Truck will start visiting the nodes and delivering the package.
        @begin_node Node Object
        @end_node Node Object
    """
    def start_delivery(self, begin_node, end_node):
        # Get the list of node routes
        list_of_node_route = self.get_node_route_list()
        if (self.debug):
            print(f"Start Delivery\n---------------\nList of Nodes to Visit")
            for node in list_of_node_route:
                self.pause()
                print(node.display())

        optimal_travel_node_path = self.optimized_travel_path(begin_node, end_node, list_of_node_route)
        if (self.debug):
            print(f"Optimal Node Path\n---------------\n")
            for node in optimal_travel_node_path:
                self.pause()
                print(node.display())
        
        # The previous_node is the starting node
        previous_node = optimal_travel_node_path[0]
        for node in optimal_travel_node_path:
            # Calculate the distance needed to travel from previous to current node
            distance_traveled = self.get_distance_between_nodes(
                previous_node.get_id(), node.get_id()
            )
            # Assumed we've traveled, keep track of cumulative distance
            self.miles_traveled += distance_traveled
            # Update the time it took to get there
            self.time_count += timedelta(hours=(distance_traveled / self.speed))

            if (self.debug):
                print(f"Truck {self.truck_id} at location {node.display()} at time " + self.time_count.strftime("%I:%M %p") + "\n")
                self.pause()

            # We are currently at this node
            self.set_current_location(node)
            # Deliver packages
            self.deliver_package()
            # We're checking the next node now
            previous_node = node
###########################################################################################
    """ Given a start node and a list of nodes to visit; dijkstra's algorithm will return a list of visited nodes with all the previous vertex, 
        and the shortest distance from the start node
        @start_node : Node Object
        @list_of_nodes : List of Node Objects
    """
    def dijkstra(self, start_node, list_of_nodes):
        # Initially each node in our node list should have their distance set infinte from the start node
        # They should also not have any previous nodes yet
        for nodes in list_of_nodes:
            nodes.set_shortest_distance(float("inf"))
            nodes.set_previous_node(None)
        # Shortest distance from start node to itself is 0 with no previous nodes
        start_node.set_shortest_distance(0.0)
        start_node.set_previous_node(None)
        # We need to keep track of visited and unvisited nodes
        visited_nodes = []
        # Make a copy of the node's list so we don't modify the reference and also include the start node
        unvisited_nodes = list(list_of_nodes)
        unvisited_nodes.append(start_node)
        # Vist every unvisited nodes
        while unvisited_nodes:
            # Find the node with the smallest known distance from the start node
            small_index = 0
            for i in range(len(unvisited_nodes)):
                if (
                    unvisited_nodes[i].get_shortest_distance()
                    < unvisited_nodes[small_index].get_shortest_distance()
                ):
                    small_index = i
            # Select the node with the smallest distance from the start, remove it from the unvisited noes
            current_node = unvisited_nodes.pop(small_index)
            # Mark the node as visited
            visited_nodes.append(current_node)
            # The truck could visit any possible node in the unvisited node next
            for nodes in unvisited_nodes:
                # Calculate the distance between the current node and the next potential node to visit
                # If it is shorter than the shortest distance on file we need to update that
                calculated_distance = (
                    current_node.get_shortest_distance()
                    + self.get_distance_between_nodes(
                        nodes.get_id(), current_node.get_id()
                    )
                )
                # Update the shortest distance if we found a shorter distance to the selected node
                if calculated_distance < nodes.get_shortest_distance():
                    nodes.set_shortest_distance(calculated_distance)
                    nodes.set_previous_node(current_node)
        # Return a list of visited nodes
        return visited_nodes
###########################################################################################
    """ Load the packages onto the truck.
    """
    def load_packages_by_id(self, list_of_package_ids):
        # For each of the package ID we want to load.
        for id in list_of_package_ids:
            # Check to see if the ID actually exists in the total package list.
            for package in self.packages_list:
                # We found the package ID in the list.
                if int(id) == int(package.get_package_id()):
                    # Check if the truck has enough space.
                    if len(self.current_packages) < self.capacity:
                        package.set_status("En route, time : " + self.time_count.strftime("%I:%M %p") + " | To Hub : " + package.get_address())
                        if (self.debug):
                            print(f"Loading Package\n----------------\n{package.display()}\nOnto Truck {self.truck_id}")
                            self.pause()
                        self.current_packages.append(package)
                    else:
                        print(f"Truck {self.truck_id} : Full not loading package : " + package.get_package_id() + "\n")
###########################################################################################
    """ Deliver appropriate packages at the current node
    """
    def deliver_package(self):
        for package in self.packages_list:
            if package in self.current_packages:
                package.set_status("En route, time : " + self.time_count.strftime("%I:%M %p") + " | To Hub : " + package.get_address())
                # Check to see if the package is at the right address
                if str(package.get_address()) == str(self.get_current_location().get_address()):
                    if (self.debug):
                        print(f"Delivering Package : {package.display()} at Location : {self.get_current_location().display()}")
                        self.pause()
                    self.current_packages.remove(package)
############################################################################################
    """ Set the current location 
    """
    def set_current_location(self, node):
        self.current_location = node
    """ Get the current location 
    """
    def get_current_location(self):
        return self.current_location
    """ Get the total miles traveled 
    """
    def get_miles_traveled(self):
        return self.miles_traveled
    """ Return the hash table of package records
    """
    def get_package_records(self):
        return self.package_records
    """ Get the truck's ID
    """
    def get_truck_id(self):
        return self.truck_id
    """ Pause execution
    """
    def pause(self):
        input("Press any key to continue...")
    """ Display Truck Information
    """
    def display(self):
        status = (
            f"Truck {self.truck_id} Status:\n"
            f"Miles Traveled: {self.miles_traveled}\n"
            f"Current Location: {self.current_node.display()}\n"
            f"Current Time: {self.time_count.strftime('%I:%M %p')}\n"
        )
        print(status)