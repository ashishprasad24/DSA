#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    
    #using a pointer to iterate over linked list.
    curr_node=head
    
    #traversing through the linked list.
    while curr_node.next:
        
        #if data at current node and next node are same, we store the node 
        #next to the next node of current node in link of current node.
        if(curr_node.data == curr_node.next.data):
            curr_node.next = curr_node.next.next
            
        #else we just move the pointer to next node.
        else:
            curr_node=curr_node.next
            
