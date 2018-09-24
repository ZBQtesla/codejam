class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(n,k,[])
        return self.result
    
    def helper(self,n,k,already):
        if not k:
            self.result.append(already)
        else:   #we choose the larger one first
            for num in range(k,n + 1):
                self.helper(num - 1,k - 1,already + [num])
