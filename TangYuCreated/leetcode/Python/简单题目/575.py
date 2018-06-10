class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        length = len(candies)
        sorts = len(set(candies))
        return min(length // 2,sorts)
