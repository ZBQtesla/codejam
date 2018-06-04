class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        
        minSoFar = max(prices)
        day = 0
        profit = 0
        while day < len(prices):
            if prices[day] < minSoFar:
                minSoFar = prices[day]
                day += 1
                continue
            if prices[day] - minSoFar > profit:
                profit = prices[day] - minSoFar
            day += 1
        return profit
