class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #The array hold has hold[i] == max profit we get at day i - 1 if we hold stocks.Have i data
        #sell[i] is the profit without stocks by hand
        length = len(prices)
        if not length:
            return 0
        hold = [0] * (length + 1)
        sell = [0] * (length + 1)
        hold[1] = -prices[0]
        for day in range(1,length):
            sell[day + 1] = max(sell[day],hold[day] + prices[day])
            hold[day + 1] = max(hold[day],sell[day - 1] - prices[day])
        return sell[-1]
