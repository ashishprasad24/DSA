
class Solution:
    
    #Function to find the height of a binary tree.
    def height(self, node):
        
        #if node is null, we return 0.
        if node is None: 
            return 0
            
        #else we call the recursive function, height for left and right 
        #subtree and choose their maximum. we also add 1 to the result
        #which indicates height of root of the tree.
        return (1 + max(self.height(node.left), self.height(node.right)))
