class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == [] or len(prices) == 1:
            return 0
        profit = 0
        for day in range(len(prices) - 1):
            profit += max(0,prices[day + 1] - prices[day])
        return profit
