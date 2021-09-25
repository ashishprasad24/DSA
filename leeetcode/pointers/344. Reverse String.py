class Solution:
    def reverseString(self, s: List[str]) -> None:
        head = 0
        tail = len(s) - 1
        
        while head < tail:
            temp = s[head]
            s[head] = s[tail]
            s[tail] = temp
            
            head += 1
            tail -= 1
        
        
