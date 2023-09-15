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
                    self.master_hash.update_linked_list(
                        i, package_record.search(i).copy()
                    )
        self.options = [
            "Option 1: Query Package by ID",
            "Option 2: Query All Packages Given Time",
            "Option 3: Query Specific Package in Time",
            "Option 4: Exit",
        ]
        self.suboptions = {
            "Option 1: Query Package by ID",
            "Option 2: Query Package by Address",
            "Option 3: Query Package by City",
            "Option 4: Query Package by State",
            "Option 5: Query Package by Zip",
            "Option 6: Query Package by Delivery Time",
            "Option 7: Query Package by Weight",
        }

    def unit_test_package_deadlines(self):
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
                if current_node.value.get_deadline() != "EOD":
                    # If the node's delivery time is greater than the expected EOD time, we did not deliver on time
                    if current_node.time.replace(
                        year=2000, month=1, day=1, second=0, microsecond=0
                    ) > datetime.strptime(
                        current_node.value.get_deadline(), "%I:%M %p"
                    ).replace(
                        year=2000, month=1, day=1, second=0, microsecond=0
                    ):
                        print(current_node.value.display())
                        print("!!! FAILED UNIT TEST !!!")
                        return False
                current_node = current_node.next
        print("!!! PASSED UNIT TEST !!!")
        return True

    def display_menu(self, subchoice):
        print("\nMenu:")
        if subchoice:
            for suboptions in self.suboptions:
                print(suboptions)
        else:
            for option in self.options:
                print(option)

    def get_choice(self, subchoice):
        while True:
            try:
                if subchoice:
                    choice = int(input("\nPlease select an option (1-7): "))
                    if 1 <= choice <= 7:
                        return choice
                    else:
                        print("Invalid choice. Please enter a number between 1 and 7.")
                else:
                    choice = int(input("\nPlease select an option (1-4): "))
                    if 1 <= choice <= 4:
                        return choice
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid choice. Please enter the valid option range")

    def search_package_given_params(self, time, **kargs):
        id = kargs.get("package_id", None)
        address = kargs.get("address", None)
        city = kargs.get("city", None)
        state = kargs.get("state", None)
        zip = kargs.get("zip", None)
        deadline = kargs.get("deadline", None)
        weight_kg = kargs.get("weight_kg", None)
        all = kargs.get("all", False)
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
                    if current_node.time.replace(
                        year=2000, month=1, day=1, second=0, microsecond=0
                    ) <= time.replace(
                        year=2000, month=1, day=1, second=0, microsecond=0
                    ):
                        # Check if it matches our extra fields
                        if (all == True):
                            print(current_node.value.display())
                            break
                        if (
                            address != None
                            and address == current_node.value.get_address()
                        ):
                            print(current_node.value.display())
                            break
                        if city != None and city == current_node.value.get_city():
                            print(current_node.value.display())
                            break
                        if state != None and state == current_node.value.get_state():
                            print(current_node.value.display())
                            break
                        if zip != None and zip == current_node.value.get_zip():
                            print(current_node.value.display())
                            break
                        if (
                            deadline != None
                            and deadline == current_node.value.get_deadline()
                        ):
                            print(current_node.value.display())
                            break
                        if (
                            weight_kg != None
                            and weight_kg == current_node.value.get_weight_kg()
                        ):
                            print(current_node.value.display())
                            break
                    current_node = current_node.next
        else:
            # Get a copy of the linked list so we don't mess with the reference
            linkedlist = self.master_hash.search(id).copy()
            linkedlist.reverse()
            current_node = linkedlist.head
            while current_node:
                if current_node.time.replace(
                    year=2000, month=1, day=1, second=0, microsecond=0
                ) <= time.replace(year=2000, month=1, day=1, second=0, microsecond=0):
                    print(
                        "Node time : "
                        + current_node.time.strftime("%H:%M")
                        + " Time : "
                        + time.strftime("%H:%M")
                    )
                    print(current_node.value.display())
                    break
                current_node = current_node.next

    def run(self):
        self.unit_test_package_deadlines()
        while True:
            self.display_menu(False)
            choice = self.get_choice(False)
            if choice == 1:
                package_id = input("Enter a package ID : ")
                self.master_hash.search(package_id).display()
                print("\nDelivered Information:")
                print(self.master_hash.search(package_id).peek_last().value.display())
            elif choice == 2:
                time = input("Enter a time in the format '9:50 AM': ")
                self.search_package_given_params(datetime.strptime(time, "%I:%M %p"), all=True)
            elif choice == 3:
                self.display_menu(True)
                subchoice = self.get_choice(True)
                time = input("Enter a time in the format '9:50 AM': ")
                if subchoice == 1:
                    package_id = input("Enter a package ID : ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), package_id
                    )
                if subchoice == 2:
                    address = input("Enter an address in the format '3060 Lester St': ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), address=address
                    )
                if subchoice == 3:
                    city = input("Enter a city in the format 'Salt Lake City': ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), city=city
                    )
                if subchoice == 4:
                    state = input("Enter a city in the format 'UT': ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), state=state
                    )
                if subchoice == 5:
                    zip = input("Enter a zip in the format '84117': ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), zip=zip
                    )
                if subchoice == 6:
                    deadline = input(
                        "Enter a deadline in the format 'EOD or 10:30 AM': "
                    )
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), deadline=deadline
                    )
                if subchoice == 7:
                    weight_kg = input("Enter a weight in the format '5': ")
                    self.search_package_given_params(
                        datetime.strptime(time, "%I:%M %p"), weight_kg=weight_kg
                    )
            elif choice == 4:
                print("Exiting...")
                break
