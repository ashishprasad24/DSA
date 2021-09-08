class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoOpen={")":"(","]":"[","}":"{"}
        
        for c in s:
            if c in closetoOpen:
                if stack and stack[-1]== closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False    
      
      #onemore
      class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True
      
