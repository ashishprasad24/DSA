
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        
        #using two pointers and moving one pointer(slow) by one node and 
        #another pointer(fast) by two nodes in each iteration.
        slow = head
        fast = head
    
        #using a loop to move the pointers which stops when any of the pointers
        #or the pointer next to fast becomes null.
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            #if both the pointers fast and slow point to same node which 
            #shows the presence of loop so we return true.
            if slow == fast :
                return True
        
        #if we reach here it means both the pointers fast and slow never 
        #point to same node so we return false.
        return False
