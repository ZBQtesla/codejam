# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #algorithmic idea:after deleting one element,we fix the subtree by appending the left branch of right-subtree of 
        #this node with the right branch's leftmost node
        #connotative condition:None
        #this function works as descibed
        if root == None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
            return root
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightMost = self.findTheRightMost(root.left)
                rightMost.right = root.right.left
                root.right.left = root.left
                
                return root.right
            
    def findTheRightMost(self,root):
        #connotative condition:root != None
        result = root
        while result.right != None:
            result = result.right
        return result
