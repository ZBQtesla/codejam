class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {i:0 for i in range(1,33)}    #1 is the lowest bit
        for num in nums:
            if num > 0 :
                for i in range(1,33):
                    dic[i] += num % 2
                    num //= 2
            elif num < 0:
                num = -num - 1
                for i in range(1,33):
                    dic[i] += (num + 1) % 2
                    num //= 2
        result = 0
        for key in sorted(dic)[:-1]:
            if dic[key] % 3:
                result += 2 ** (key - 1)
        result += -(dic[32] % 3) * 2 ** 31
        return result
