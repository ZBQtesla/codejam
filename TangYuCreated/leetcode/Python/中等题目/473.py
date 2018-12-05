class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 4:
            return False
        else:
            self.target = sum(nums) // 4
        if not nums or len(nums) < 4:
            return False
        return self.backpack(nums,4)
    
    def backpack(self,nums,num_pack):
        if num_pack == 1:
            return True if sum(nums) == self.target else False
        numsLen = len(nums)
        if sum(nums) != self.target * num_pack:
            return False
        
        already = []    #our first backpack
        length = 0  #the number of items in our first backpack
        nextPos = 0 #the position of the next item to be added
        weight = 0
        
        nums.sort()
        while weight < self.target:
            if nextPos < numsLen:   #valid pos
                already.append((nextPos,nums[nextPos]))
                weight += nums[nextPos]
                length += 1
                nextPos += 1
            else:
                found = False
                for pos in range(length - 1):
                    if already[pos][0] - already[pos + 1][0] < -1:
                        found = True
                        lastOne = pos
                if not found:
                    return False
                else:
                    nextPos = already[lastOne][0] + 1
                    already = already[:lastOne]
                    weight = sum([element[0] for element in already])
                    length = len(already)
            
            if weight == self.target:
                chosen = {element[0] for element in already}
                leftover = [nums[i] for i in range(numsLen) if i not in chosen]
                if self.backpack(leftover,num_pack - 1):
                    return True
                else:
                    lastIndex,lastWeight = already.pop()
                    weight -= lastWeight
                    length -= 1
                    nextPos = lastIndex + 1
                    if length == 0:
                        return False
                    else:
                        lastIndex,lastWeight = already.pop()
                        weight -= lastWeight
                        length -= 1
                        nextPos = lastIndex + 1
            elif weight > self.target:
                lastIndex,lastWeight = already.pop()
                weight -= lastWeight
                length -= 1
                nextPos = lastIndex + 1
                if length == 0:
                    return False
                else:
                    lastIndex,lastWeight = already.pop()
                    weight -= lastWeight
                    length -= 1
                    nextPos = lastIndex + 1
