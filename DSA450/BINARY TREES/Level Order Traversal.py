
class Solution:
    
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        
        res = []
        
        #if node is null, we return the list.
        if root is None:
            return res
            
        #creating an empty queue for level order traversal.
        que = []
        que.append(root)
        
        while 1:
            n = len(que)
            if n==0:
                break
            while(n>0):
                #storing front element of queue in list and 
                #removing it from queue.
                node = que.pop(0)
                res.append (node.data)
                
                #storing the left child of the parent node in queue.
                if node.left != None:
                    que.append(node.left)
                    
                #storing the right child of the parent node in queue.
                if node.right != None:
                    que.append(node.right)
                n-=1
                
        #returning the list.
        return res
        
