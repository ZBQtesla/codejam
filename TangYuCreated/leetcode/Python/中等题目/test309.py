class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #reference[i] is the maximum profit we can get if we have only
        #prices[0],...,prices[i - 1]
        length = len(prices)
        reference = [0] * (length + 1)
        for last in range(1,length):
            reference[last + 1] = max([prices[last] - prices[i] + reference[max(0,i - 1)] for i in range(last)] + [reference[last]])
        return reference[-1]
solution = Solution()
print(solution.maxProfit([1,4,2]))
