class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        self.mergetreenodes(t1,t2)
        return t1
    
    
    def mergetreenodes(self,root1,root2):
        '''type roo1:TreeNode
            type roo2:TreeNode
            rtype:None
        '''
        #comebine them to root1
        root1.val += root2.val
        if root1.left == None:
            root1.left = root2.left
        elif root1.left != None and root2.left != None:
            self.mergetreenodes(root1.left,root2.left)
            
        if root1.right == None:
            root1.right = root2.right
        elif root1.right != None and root2.right != None:
            self.mergetreenodes(root1.right,root2.right)        
