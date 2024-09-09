class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def del_node(head,pos):
    temp=head
    prev =None
        
    if temp == None:
        return None
        
        #for deletio of head
    if pos == 1:
        head= temp.next
        return head
        
        #for Node which needs to be deleted is in middle
        
    for i in range(1,pos):
        prev = temp
        temp = temp.next
        if temp is None:
            print("data is not present")
            return head
        
    if temp is not None:
        prev.next = temp.next
        
    return head
def print_list(head):
        while head:
            print(f"{head.data}->",end="")
            head= head.next
        print("None")
        
if __name__ == "__main__":
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(55)
        head .next.next.next.next= Node(9)
        print_list(head)
        position = 2
        head = del_node(head,position)
        print_list(head)
        
        
        
        
        