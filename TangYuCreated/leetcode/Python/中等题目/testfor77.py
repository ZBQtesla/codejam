class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        present = -1
        already = [None] * k
        mini = 1
        while True:
            if present < k - 1:
                print('mini is:',mini,present)
                already[present + 1] = mini
                mini += 1
                present += 1
            else:
                print(already)
                result.append(already[:])
                print('mini in else before addition is:',mini)
                print('mini in else is:',mini)
                present -= 1
                if mini > n:
                    already[present] += 1
                    while already[present] - present > n - k + 1:
                        present -= 1
                        if present == -1:
                            return result
                        already[present] += 1
                    mini = already[present] + 1

solution = Solution()
print(solution.combine(6,2))
