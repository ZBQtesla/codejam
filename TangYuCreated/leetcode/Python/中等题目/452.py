class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x:x[0])
        ends = sorted([point[1] for point in points])
        result = 0
        while ends:
            target = ends[0]
            num = 0
            result += 1
            for point in points:
                if point[0] <= target:  #this ballon explodes
                    num += 1
                else:
                    break
            for point in points[:num]:
                ends.remove(point[1])
            del points[:num]
        return result
