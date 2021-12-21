
class Solution:
    dia=0
    
    #Function to find the diameter of a Binary Tree.
    def util(self,root):
        
        #if node becomes null, we return 0.
        if root == None:
            return 0
        global dia
        
        #calling the util function recursively for the left and 
        #right subtrees to find their heights.
        l=self.util(root.left)
        r=self.util(root.right)
        
        #storing the maximum possible value of l+r+1 in diameter.
        dia=max(dia, l+r+1)
        
        #returning height of subtree.
        return 1 + max(l, r)
    
  
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        global dia
        dia=0
        #calling the function to find the result.
        self.util(root)
        #returning the result.
        return dia
