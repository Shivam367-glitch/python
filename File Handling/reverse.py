class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head)

# Reverse the linked list
head = reverseLinkedList(head)

print("Reversed linked list:")
printLinkedList(head)
