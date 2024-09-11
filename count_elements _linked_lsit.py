#counting an element  in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def counts(head):
    count = 0
    while head is not None:
        count = count+1
        head =  head.next
        
    return count
# Driver code
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 3 -> 1 -> 2 -> 1
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
 

    # Function call to count the number of nodes
    print("Count of nodes is ", counts(head))