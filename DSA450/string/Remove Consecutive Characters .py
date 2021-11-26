
class Solution:
    def removeConsecutiveCharacter(self, s):
        st = []
    
        for i in range(len(s)):
    
            if (st and st[-1] != s[i]) or not st:
                st.append(s[i])
        res = ''
    
        while st:
            res += st.pop()
    
        return res[::-1]
                
