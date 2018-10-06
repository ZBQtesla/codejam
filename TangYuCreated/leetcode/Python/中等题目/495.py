class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        result = 0
        for first in range(len(timeSeries) - 1):
            result += min(timeSeries[first + 1] - timeSeries[first],duration)
        result += duration
        return result
