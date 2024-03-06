class Node:
    
    def __init__(self,data) :
        self.data=data
        self.next=None


class LinkedList:
    
    def __init__(self):
        self.head=None
    
     # Method to insert a new node at the end of the linked list
    def append(self,data):
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            
    def delete_from_end(self):
        if self.head is None:
            return
        
        # only one node is in linkedlist
        if self.head.next is None:
            self.head=None
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        
        temp.next=None
            
        
             
    # Method to print the linked list     
    def print_List(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def reverseLinkedList(self):
        curr=self.head
        pre=None
        next=None
        
        while curr is not None:
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        self.head=pre
        
            
if __name__ == "__main__":
    linkedList=LinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.print_List()
    linkedList.reverseLinkedList()
    print("After reversing:")
    linkedList.print_List()
    print("After Deleting Last Node:")
   
    linkedList.delete_from_end()
    linkedList.print_List()
           
        
                    
                
        
        
    