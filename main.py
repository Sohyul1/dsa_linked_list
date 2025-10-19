# main.py
from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    print("=== INSERTING NODES ===")
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_beginning(5)
    ll.print_list()  

    print("\n=== SEARCHING FOR VALUES ===")
    print("Search 20:", ll.search(20))  
    print("Search 99:", ll.search(99)) 

    print("\n=== REMOVING ELEMENTS ===")
    print("Removed from beginning:", ll.remove_beginning())   
    print("Removed from end:", ll.remove_at_end())          
    print("Removed specific (20):", ll.remove_at(20))        
    ll.print_list()  

    print("\n=== ADDING MORE ELEMENTS ===")
    ll.insert_at_end(50)
    ll.insert_at_beginning(1)
    ll.print_list()  

    print("\n=== FINAL SEARCH TESTS ===")
    print("Search 50:", ll.search(50))  
    print("Search 100:", ll.search(100)) 

    print("\n=== FINAL LIST STATE ===")
    ll.print_list()
