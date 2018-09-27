class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        length = len(prices)
        if not length:
            return 0
        buy = [0] * length
        sell = [0] * length
        buy[0] = -fee - prices[0]
        for day in range(1,length):
            sell[day] = max(sell[day - 1],buy[day - 1] + prices[day])
            buy[day] = max(buy[day - 1],sell[day - 1] - prices[day] - fee)
        return sell[-1]
