class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        maxleft = 0
        minleft = prices[0]
        profitLeft = []
        for price in prices:
            minleft = min(minleft,price)
            maxleft = max(price - minleft,maxleft)
            profitLeft.append(maxleft)
        
        maxProfitRight = 0
        maxRight = prices[-1]
        profitRight = []
        for price in prices[::-1]:
            maxRight = max(price,maxRight)
            maxProfitRight = max(maxRight - price,maxProfitRight)
            profitRight.append(maxProfitRight)
        profitRight.reverse()
        return max( [profitLeft[day] + profitRight[day] for day in range(len(prices))])
