#reversal of linked list

class Node:
    def __init__(self,data):
        self.data= data
        self.next =None

def rev_list(head):
    curr = head
    prev = None
    
    while curr is not None:
        
        next_node = curr.next
        curr.next  = prev 
        
        prev =  curr
        curr = next_node
    return prev

def print_list(node):
    while node is not None:
        print(f" {node.data} ", end="")
        node = node.next
    print()    
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    print("linked_list before sort is ")
    print_list(head)
    
    
    head = rev_list(head)
    print("linked list after sorting is :")
    print_list(head)
        
        