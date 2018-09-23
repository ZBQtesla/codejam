class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        reference = [max(piles[i],piles[i + 1]) for i in range(len(piles) - 1)]
        length = len(reference)
        for iteration in range(1,len(piles) // 2):
            for pos in range(length - 2 * iteration + 1):
                reference[pos] = min(reference[pos],reference[pos + 1])
            for pos in range(length - 2 * iteration):
                reference[pos] = max(reference[pos] + piles[pos + 2 * iteration + 1],reference[pos + 1] + piles[pos])
        return 2 * reference[0] > sum(piles)
