class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        end=float("-inf")
        points.sort(key=lambda p:p[1])
        for s, e in points:
            if s>end:
                ans+=1
                end = e
        return ans
