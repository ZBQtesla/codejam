class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.Result = []
        self.generate([],nums)
        return self.Result
    
    def generate(self,subpermu,List):
        if len(List) == 1:
            self.Result.append(subpermu + [List[0]])
        else:
            for i in range(len(List)):
                self.generate(subpermu + [List[i]] , List[:i] + List[i + 1:])
