class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        
        left,right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True    
        
