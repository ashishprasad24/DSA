#User function Template for python3
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        
        #default dict to store mapping of characters.
        d=defaultdict(chr) 
        
        if(len(str1)  != len(str2)):
            return False
            
        #using a boolean array to mark visited characters in str2.
        marked=[0 for i in range(26)] 
        
        for i in range(len(str1)):
            c=str1[i]
            c_p=str2[i]
            
            #if current character of str1 is seen first time in dict.
            if(c not in d):
                
                #if current character of str2 is already
                #seen, one to one mapping is not possible.
                if(marked[ord(c_p)-ord('a')]):
                    return False
                else:
                    #marking current character of str2 as visited.
                    marked[ord(c_p)-ord('a')]=1
                    #storing mapping of current characters.
                    d[c]=c_p
                    
            #if this isn't first appearance of current character in str1 then
            #checking if previous appearance mapped to same character of str2.
            else:
                if(d[c] != c_p):
                    return False
        return True
                
