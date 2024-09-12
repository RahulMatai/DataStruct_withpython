#doubley lin ked list insertion at start
class node:
    def __init__(self,new_data):
        self.data = new_data
        self.next =None
        self.prev = None
def insert_node(head,new_data):
    new_node= node(new_data)
    
    new_node.next = head
   
    
    if head is not None:
        head.prev = new_node
        
    return new_node

def print_list(head):
    curr =  head
    while curr is not  None:
        print(f"{curr.data}",end="")
        curr =  curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 2 <-> 3 <-> 4
    head = node(2)
    head.next = node(3)
    head.next.prev = head
    head.next.next = node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end='')
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Node at the front:", end='')
    data = 1
    head = insert_node(head, data)

    # Print the updated list
    print_list(head)
    