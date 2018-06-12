class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        counts = 121 * [0]
        for age in ages:
            counts[age] += 1
        
        leftEdge = 68
        total = sum(counts[leftEdge:])
        count = 0
        for age in range(120,14,-1):     #when kids are younger than 15 years old,they cannot send a card
            newLeftEdge = int(age * 0.5) + 8
            if newLeftEdge != leftEdge:
                total += counts[newLeftEdge]
            leftEdge = newLeftEdge
            
            if counts[age]:
                num = counts[age]
                count += num * (num - 1) + num * (total - num)
                total -= counts[age]
        return count
