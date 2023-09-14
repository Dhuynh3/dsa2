from hashtable import HashTable
from datetime import datetime, timedelta

class Interface:
    def __init__(self, array_of_package_records):
        self.bucket_size = array_of_package_records[0].get_size()
        self.master_hash = HashTable(self.bucket_size)
        # For each hash table record
        for package_record in array_of_package_records:
            # Peek through all of the buckets
            for i in range(self.bucket_size):
                # Search the hashtable and peek into the linked list
                # If something exists, add it to the master_hash table
                if package_record.search(i).peek():
                    # Update the linked list in this bucket
                    self.master_hash.update_linked_list(i, package_record.search(i).copy())
        self.options = [
            "Option 1: Query Package by ID",
            "Option 2: Query All Packages Given Time",
            "Option 3: Query Specific Package in Time",
            "Option 4: Exit"
        ]
    def display_menu(self):
        print("\nMenu:")
        for option in self.options:
            print(option)

    def get_choice(self):
        while True:
            try:
                choice = int(input("\nPlease select an option (1-4): "))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 4.")
    def search_package_given_params(self, time, id=None, address=None):
        # If we didnt specify an ID
        if id == None:
            # Go through every single index
            for i in range(self.bucket_size):
                # Get a copy of the linked list so we don't mess with the reference
                linkedlist = self.master_hash.search(i).copy()
                # Reversing the list now shows the latest time first
                linkedlist.reverse()
                # Loop through the nodes and print the information of the 
                # first instance record of the package that is less than the time given
                current_node = linkedlist.head
                while current_node:
                    # It is less than the given time.
                    if current_node.time.replace(year=2000, month=1, day=1, second=0, microsecond=0) <= time.replace(year=2000, month=1, day=1, second=0, microsecond=0):
                        # Check if it matches our extra fields
                        if (address == current_node.value.get_address()):
                            print(current_node.value.display())
                            break

                        print(current_node.value.display())
                        break
                    current_node = current_node.next
        else: 
            # Get a copy of the linked list so we don't mess with the reference
            linkedlist = self.master_hash.search(id).copy()
            linkedlist.reverse()
            current_node = linkedlist.head
            while current_node:
                if current_node.time.replace(year=2000, month=1, day=1, second=0, microsecond=0) <= time.replace(year=2000, month=1, day=1, second=0, microsecond=0):
                    print("Node time : " + current_node.time.strftime("%H:%M") + " Time : " + time.strftime("%H:%M"))
                    print(current_node.value.display())
                    break
                current_node = current_node.next
            

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_choice()
            if choice == 1:
                package_id = input("Enter a package ID : ")
                self.master_hash.search(package_id).display()
                print("\nDelivered Information:")
                print(self.master_hash.search(package_id).peek_last().value.display())
            elif choice == 2:
                time = input("Enter a time in the format '9:50 AM': ")
                self.search_package_given_params(datetime.strptime(time, "%I:%M %p"))
            elif choice == 3:
                time = input("Enter a time in the format '9:50 AM': ")
                package_id = input("Enter a package ID : ")
                self.search_package_given_params(datetime.strptime(time, "%I:%M %p"), package_id)
            elif choice == 4:
                print("Exiting...")
                break
          