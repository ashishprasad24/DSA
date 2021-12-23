class Solution:
    
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        
        if root is None:
            return None
            
        #if either n1 or n2 matches with data at current node, we return root.
        # (Note that if a node is ancestor of other, then the ancestor node
        #becomes the lowest common ancestor).
        if root.data == n1 or root.data == n2:
            return root
            
        #calling the lca function recursively for left and right subtrees.
        left_lca = self.lca(root.left, n1, n2) 
        right_lca = self.lca(root.right, n1, n2)
        
        #if both of the above calls return non-NULL value then one node
        #is present in one subtree and other is present in another subtree. 
        #So, this node is the lowest common ancestor.
        if left_lca and right_lca:
            return root
            
        #else we check if left subtree or right subtree is the
        #lowest common ancestor.
        if left_lca is not None:
            return left_lca
        else:
            return right_lca
            
