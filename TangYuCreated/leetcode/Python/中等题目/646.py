class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        pairs.sort(key = lambda pair:pair[1])
        present = pairs[0][0] - 1
        length = 0
        for pair in pairs:
            if pair[0] > present:
                present = pair[1]
                length += 1
        return length
