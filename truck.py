from hashtable import HashTable
from datamanager import DataManager

class Truck(DataManager):
    def __init__(self, truck_id, start_time, capacity=16):
        super().__init__()
        self.truck_id = truck_id
        self.start_time = start_time
        self.capacity = capacity
        self.speed = 18
        self.current_node = self.nodes_list[0]
        self.package_records = HashTable(len(self.packages_list))
        self.miles_traveled = 0
        self.current_packages = []
        
    # Load the packages onto the truck
    def load_package_by_id(self, package_id_list):
        # For each of the package ID we want to load
        for id in package_id_list:
            # Check to see if the ID actually exists in the total package list
            for package in self.packages_list:
                # We found the package ID in the list
                if int(id) == int(package.get_package_id()):
                    # Check if the truck has enough space
                    if self.capacity > len(self.current_packages):
                        print("")
                    
                    # Unable to load package, not enough space
                    else:
                        break


    # Check if we have a package to deliver at the current node
    def deliver_package(self):
        return


    def get_package_records(self):
        return self.package_records
    def get_truck_id(self):
        return self.truck_id