class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        length = len(seats)
        firstPos = seats.index(1)
        present = length
        maxLength = 0
        
        for pos in range(length):
            if seats[pos]:
                lastPos = pos
                present,previous = pos,present
                
                if (present - previous) // 2 > maxLength:
                    maxLength = (present - previous) // 2
        
        return max(maxLength,firstPos,length - 1 -lastPos)
