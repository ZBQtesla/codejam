class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.permutation = []
        self.generate(nums,[])
        for permu in self.permutation:
            if self.possible(permu):
                return True
        return False
    
    def possible(self,nums):
        if len(nums) == 1:
            return abs(24 - nums[0]) < 1e-6
        elif len(nums) == 2:
            outcome = [self.possible([val]) for val in self.tryOp(nums)]
            return True in outcome
        elif len(nums) == 3:
            left = self.tryOp(nums[:2])
            right = self.tryOp(nums[1:])
            outcomeLeft = [self.possible([val,nums[-1]]) for val in left]
            outcomeRight = [self.possible([nums[0],val]) for val in right]
            return True in (outcomeLeft + outcomeRight)
        else:
            left = self.tryOp(nums[:2])
            middle = self.tryOp(nums[1:3])
            right = self.tryOp(nums[2:])
            outcomeLeft = [self.possible([val,nums[2],nums[3]]) for val in left]
            outcomeMiddle = [self.possible([nums[0],val,nums[-1]]) for val in middle]
            outcomeRight = [self.possible([nums[0],nums[1],val]) for val in right]
            return True in (outcomeLeft + outcomeRight + outcomeMiddle)
        
        
    def tryOp(self,twoNum):
        try:
            return sum(twoNum),twoNum[0] - twoNum[1],twoNum[0] * twoNum[1],twoNum[0] / twoNum[1]
        except:
            return sum(twoNum),twoNum[0] - twoNum[1],twoNum[0] * twoNum[1]
    
    def generate(self,nums,permu):
        if len(nums) == 1:
            self.permutation.append(permu + [nums[0]])
        else:
            for i in range(len(nums)):
                self.generate(nums[:i] + nums[i + 1:],permu + [nums[i]])
