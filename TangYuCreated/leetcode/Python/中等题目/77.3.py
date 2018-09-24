class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [
                [i] for i in range(1,n + 1)
            ]
        result = []
        present = -1
        already = [None] * k
        mini = 1
        while True:
            if present < k - 1:
                already[present + 1] = mini
                mini += 1
                present += 1
            else:
                result.append(already[:])
                present -= 1
                if mini > n:
                    already[present] += 1
                    while already[present] - present > n - k + 1:
                        present -= 1
                        if present == -1:
                            return result
                        already[present] += 1
                    mini = already[present] + 1

