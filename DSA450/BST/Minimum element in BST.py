def minValue(root):
    
    #base case
    if root is None:
        return -1
    temp=root
    
    #leftmost node is minimum so we move in BST till left node is not NULL.
    while(temp.left is not None):
        temp=temp.left
        
    #returning the data at leftmost node.
    return temp.data
