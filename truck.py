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
        self.truck_node_route = None
        self.greedy_path = []

    # """ Once Dijkstra's Algorithm is finished, given an end node we can transverse it's previous node
    # to find the shortest route/path from the selected node to it's end node"""
    # def previous_node_path(self, end_node):
    #     path = SinglyLinkedList()
    #     while end_node.get_previous_node() != None:
    #         path.prepend_node(end_node)
    #         end_node = end_node.get_previous_node()
    #     return path

    # # Greedy implementation of Dijkstra's Algorithm
    # # start_node : Node Object
    # # end_node : Node Object
    # def generate_greedy_path(self, start_node, end_node):
    #     # Start at the given start node
    #     self.shortest_path.append_node(start_node)
    #     # We we still have a list of nodes to visit
    #     while self.node_route:
    #         # The algorithm will find the shortest distance from a given start node to a list of nodes to visit
    #         visited_nodes = self.dijkstra(start_node, self.node_route)
    #         # Clean the start node it has a shortest distance of 0.0 to itself
    #         for node in visited_nodes:
    #             if node.get_previous_node() == None:
    #                 visited_nodes.remove(node)
    #         # In case reaching this node with the shortest distance from our selected node that has a previous node, we need to reconstruct the path of the previous node       
    #         min_node = min(visited_nodes, key=lambda node: node.shortest_distance_from_selected_node)
    #         # We've reconstructed the path to this node with the shortest distance
    #         complete_path = self.previous_node_path(min_node)
    #         # Go through the rebuilt list from the ground up
    #         current_node = complete_path.dequeue()
    #         while current_node:
    #             self.shortest_path.append_node(current_node)
    #             self.node_route.remove(current_node)
    #             start_node = current_node
    #             current_node = complete_path.dequeue()
    #     # End with the given end node
    #     self.shortest_path.append_node(end_node)
    #     # Return the greedy path
    #     return self.shortest_path


    # def start_delivery(self, start_node, end_node):
    #     priority_queue = self.generate_greedy_path(start_node, end_node)
    #     current_node = priority_queue.dequeue()
    #     previous_node = current_node
    #     while current_node:
    #         print(current_node.display())
    #         distance_traveled = self.get_distance_between_nodes(
    #             previous_node.get_id(), current_node.get_id()
    #         )
    #         self.miles_traveled += distance_traveled
    #         self.time_count += timedelta(hours=(distance_traveled / self.speed))
    #         self.deliver_package(current_node)
    #         previous_node = current_node
    #         current_node = priority_queue.dequeue()

    def reconstruct_path(self, end_node):
        path = []
        while end_node.get_previous_node() != None:
            path.append(end_node)
            end_node = end_node.get_previous_node()
        return path[::-1]
    
    def start_delivery(self, begin_node, end_node):
        optimal_travel_node_path = []
        start_node = begin_node
        optimal_travel_node_path.append(start_node)
        while self.truck_node_route:
            visited_node_list = self.dijkstra(
                start_node, self.truck_node_route
            )
            for node in visited_node_list:
                if node.get_previous_node() == None:
                    visited_node_list.remove(node)
            min_node = min(
                visited_node_list,
                key=lambda node: node.shortest_distance_from_selected_node,
            )
            # print("Minimum Distance Node Founds | " + str(min_node))
            reconstructed_path = self.reconstruct_path(min_node)
            optimal_travel_node_path.append(reconstructed_path[0])
            # for node in reconstructed_path:
            #     print("Node : " + str(node.get_node_id()))
            self.truck_node_route.remove(min_node)
            start_node = reconstructed_path[0]

        optimal_travel_node_path.append(begin_node)
        print("----++++-----")
        for node in optimal_travel_node_path:
            print(node.display())
        print("----++++-----")

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
            # We are currently at this node
            self.set_current_location(node)
            # Deliver packages
            print("What the fuck am I doing")
            self.deliver_package()
            # We're checking the next node now
            previous_node = node
   
    

    # start_node : Node Object
    # list_of_nodes : List of Node Objects
    # Given a start node and a list of nodes to visit, dijkstra's algorithm will return a list of visited nodes with all the previous vertex, and the shortest distance from the start node
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
                        # # When loading any package onto the truck, log the current package status in our hash table
                        # self.package_records.insert(
                        #     package.get_package_id(),
                        #     ListNode(
                        #         package.snapshot(),
                        #         int(package.get_package_id()),
                        #         self.time_count,
                        #     ),
                        # )
                    else:
                        print(
                            f"Truck {self.truck_id} : Full not loading package : "
                            + package.get_package_id()
                        )
        # # We have loaded the packages based on a given ID, now make a list of nodes we have to visit based on package address
        # # For each package that is loaded.
        # truck_route_list = []
        # for package in self.current_packages:
        #     # Check against each node's address.
        #     for node in self.nodes_list:
        #         # If the package is meant for the node, add it to our node route.
        #         if package.get_address() == node.get_address():
        #             # Multiple packages may go to the same node, don't add duplicates
        #             if node not in truck_route_list:
        #                 # Add the node to the route
        #                 truck_route_list.append(node)
        # self.truck_node_route = truck_route_list

    def generate_route_list(self):
        truck_route_node_list = []
        for package in self.current_packages:
            for node in self.nodes_list:
                # Match package address with node address, but we need to make sure we haven't added the node twice
                if str(package.get_address()) == str(node.get_address()):
                    # print("Pkg ID : " + str(package.get_package_id()) + " Pkg Address : " + package.get_package_address() + " | Node ID : " + str(node.get_node_id()) + " Node Address : " + node.get_address())
                    truck_route_node_list.append(node)

        no_duplicates = []
        [
            no_duplicates.append(x)
            for x in truck_route_node_list
            if x not in no_duplicates
        ]

        self.truck_node_route = no_duplicates

        return truck_route_node_list

    # Deliver appropriate packages at the current node
    def deliver_package(self):
        # for package in self.packages_list:
        #     if package in self.current_packages:
        #         # Check to see if the package is at the right address
        #         if str(package.get_address()) == str(self.get_current_location().get_address()):
        #             print("I dropped this shit off" + package.display())
        #             self.current_packages.remove(package)

        for package in self.current_packages:
            # Check to see if the package is at the right address
            if str(package.get_address()) == str(self.get_current_location().get_address()):
                print("I dropped this shit off" + package.display())
                self.current_packages.remove(package)

    

    # Set the current location
    def set_current_location(self, node):
        self.current_location = node

    # Get the current location
    def get_current_location(self):
        return self.current_location

    # Get the total miles traveled
    def get_miles_traveled(self):
        return self.miles_traveled

    # Return the hash table of package records
    def get_package_records(self):
        return self.package_records

    # Get the truck's ID
    def get_truck_id(self):
        return self.truck_id

    # Display Truck Information
    def display(self):
        status = (
            f"Truck {self.truck_id} Status:\n"
            f"Miles Traveled: {self.miles_traveled}\n"
            f"Current Location: {self.current_node.display()}\n"
            f"Current Time: {self.time_count.strftime('%I:%M %p')}\n"
        )
        print(status)