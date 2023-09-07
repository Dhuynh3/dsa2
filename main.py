from linkedlist import SinglyLinkedList
from linkedlist import ListNode
from hashtable import HashTable
from package import Package




if __name__ == "__main__":

    # singly_linked_list = SinglyLinkedList()
    # singly_linked_list.insert_node(ListNode("Hey"))
    # singly_linked_list.insert_node(ListNode("Hey1"))
    # singly_linked_list.insert_node(ListNode("Hey2"))
    # singly_linked_list.insert_node(ListNode("Hey3"))
    # singly_linked_list.display()

    
    hash_table = HashTable(16)

    package1 = Package(package_id = 1)
    package2 = Package(package_id = 2)
    package3 = Package(package_id = 3)
    package4 = Package(package_id = 1)

    hash_table.hash_insert(package1.get_package_id(), ListNode(package1))
    hash_table.hash_insert(package2.get_package_id(), ListNode(package2))
    hash_table.hash_insert(package3.get_package_id(), ListNode(package3))
    hash_table.hash_insert(package4.get_package_id(), ListNode(package4))
    hash_table.display()

 
    print("Alive")