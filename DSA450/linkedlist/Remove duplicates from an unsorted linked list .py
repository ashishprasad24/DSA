class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        
         #using set to store already seen values in list. 
        hash=set() 
    
        #using two pointers one of which stores first node other null.
        curr = head
        prev= None
        
        #traversing over the linked list.
        while curr is not None:
            
            #if data at current node is already present in set, we skip the 
            #current node and store the node next to current in link of prev. 
            if curr.data in hash:
                prev.next = curr.next
                #deleting current node which contains duplicates. 
                del curr
            
            #else we just insert the data at current node in set and update 
            #prev to the current node.
            else:
                hash.add(curr.data)
                prev=curr
                
            #updating current to the next node of prev node.
            curr = prev.next
        
        return head
