class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
def del_head(head):
        if head is None:
            return None
        
        temp = head #value for head to temp for deletion
        head = head.next
        
        del temp
        
        return head
    
def print_lis(head):
        while head:
            print(head.data, end="->")
            head = head.next
        print("None")
        
if __name__ == "__main__":
        head = Node(1)
        head.next = Node(2)
        head.next.next= Node(3)
        head.next.next.next = Node(4)
        print("list = ")
        print_lis(head)
        head = del_head(head)
        print("List after deletion")
        print_lis(head)