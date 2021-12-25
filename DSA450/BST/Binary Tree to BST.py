class Solution:
    def binaryTreeToBST(self, root): 
        # Base Case: Tree is empty 
        if root is None: 
            return
        
        # Create the temp array and store the inorder traveral  
        # of tree  
        arr = [] 
        self.storeInorder(root, arr) 
        
        # Sort the array 
        arr.sort() 
        
        # copy array elements back to binary tree 
        self.arrayToBST(arr, root) 
    
    def storeInorder(self, root, inorder): 
        # Base Case 
        if root is None: 
            return 
        
        # First store the left subtree 
        self.storeInorder(root.left, inorder) 
        
        # Copy the root's data 
        inorder.append(root.data) 
        
        # Finally store the right subtree 
        self.storeInorder(root.right, inorder) 
    
    def arrayToBST(self, arr, root): 
        # Base Case 
        if root is None: 
            return 
        
        # First update the left subtree 
        self.arrayToBST(arr, root.left) 
        
        # now update root's data delete the value from array 
        root.data = arr[0] 
        arr.pop(0) 
        
        # Finally update the right subtree 
        self.arrayToBST(arr, root.right) 
