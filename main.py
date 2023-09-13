from linkedlist import SinglyLinkedList
from linkedlist import ListNode
from hashtable import HashTable
from package import Package
from truck import Truck



# Entry point
if __name__ == "__main__":

    # truck_one = Truck(1, "8:00 AM", 16)
    # truck_one.load_packages_by_id([1, 13, 14, 15, 16, 19, 20, 23, 29, 30, 31, 33, 34, 37, 39, 40])
    # truck_one.start_delivery(truck_one.nodes_list[0], truck_one.nodes_list[0])
 
    # truck_one.load_packages_by_id([2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22])
    # truck_one.start_delivery(truck_one.nodes_list[0], truck_one.nodes_list[0])

    truck_two = Truck(2, "8:00 AM", 16, True)
    truck_two.load_packages_by_id([3, 18, 36, 38, 24, 26, 27, 35])
    truck_two.start_delivery(truck_two.nodes_list[0], truck_two.nodes_list[0])

    truck_two.load_packages_by_id([6, 25, 28, 32])
    truck_two.start_delivery(truck_two.nodes_list[0], truck_two.nodes_list[0])


    # truck_one.display()
    truck_two.display()



    print("Alive")