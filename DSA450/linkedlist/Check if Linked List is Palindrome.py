class Solution:
    # solution
    
    
    #Function to reverse a linked list.
    def reverseList(self, temp):  
        current = temp;  
        prevNode = None;  
        nextNode = None;  
          
        while(current != None):  
            nextNode = current.next;  
            current.next = prevNode;  
            prevNode = current;  
            current = nextNode;  
        return prevNode;  
              
    
    
    #Function to return the size of linked list.
    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count
    
    #Function to check whether the list is palindrome.
    def isPalindrome(self, head):  
        current = head;  
        flag = True;  
        
        #finding number of nodes in the list.  
        s = self.getSize(head)
        mid = (s//2) if(s%2 == 0) else ((s+1)//2);  
          
        #finding the middle node in given singly linked list.  
        for i in range(1, mid):  
            current = current.next;  
              
        #reversing the list after middle node to end. 
        revHead = self.reverseList(current.next);  
          
        #comparing nodes of first half and second half of list.  
        while(head != None and revHead != None):  
            if(head.data != revHead.data):  
                flag = False;  
                break;  
                  
            head = head.next;  
            revHead = revHead.next;  
        
        #returning 1 if list is palindrome else 0.    
        return flag
