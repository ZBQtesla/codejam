class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        #connotative condition:None
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        elif d == 2:                        #we have to guarantee that we don't go into a None node
            newLeft = TreeNode(v)
            newRight = TreeNode(v)
            newLeft.left = root.left
            newRight.right = root.right
            root.left = newLeft
            root.right = newRight
            return root
        else:                               #depth >= 3
            if root.left != None:
                root.left = self.addOneRow(root.left,v,d - 1)
            if root.right != None:
                root.right = self.addOneRow(root.right,v,d - 1)
            return root
