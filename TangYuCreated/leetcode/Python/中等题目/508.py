# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dic = {}
        target = []
        maxAppearance = 0
        self.getTheSubtreeSum(root)
        for key in self.dic:
            if self.dic[key] > maxAppearance:
                target = [key]
                maxAppearance = self.dic[key]
            elif self.dic[key] == maxAppearance:
                target.append(key)
        return target
    
    def getTheSubtreeSum(self,root):
        if not root.left and not root.right:
            target = root.val
            if target in self.dic:
                self.dic[target] += 1
            else:
                self.dic[target] = 1
            return target
        elif not root.left:
            target = root.val + self.getTheSubtreeSum(root.right)
            if target in self.dic:
                self.dic[target] += 1
            else:
                self.dic[target] = 1
            return target
        elif not root.right:
            target = root.val + self.getTheSubtreeSum(root.left)
            if target in self.dic:
                self.dic[target] += 1
            else:
                self.dic[target] = 1
            return target
        else:
            target = root.val + self.getTheSubtreeSum(root.right) +\
            self.getTheSubtreeSum(root.left)
            
            if target in self.dic:
                self.dic[target] += 1
            else:
                self.dic[target] = 1
            return target
