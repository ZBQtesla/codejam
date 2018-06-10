class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        outcome = [6]
        while outcome[-1] < K:
            outcome.append(outcome[-1] * 5 + 1)
        for i in range(len(outcome) - 1,-1,-1):
            K %= outcome[i]
            if K + 1== outcome[i]:
                return 0
        return 5
