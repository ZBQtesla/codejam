class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = [0] * n
        if k == 1:
            return list(range(1,n + 1))
        if k % 2 == 0:
            for iteration in range(k // 2):
                result[iteration * 2] = iteration + 1
                result[iteration * 2 + 1] = n - iteration
            else:
                pos = iteration * 2 + 1
                result[pos + 1:] = range(result[pos] - 1,result[pos - 1],-1)
        else:
            for iteration in range(k // 2):
                result[iteration * 2] = iteration + 1
                result[iteration * 2 + 1] = n - iteration
            else:
                pos = iteration * 2 + 2
                result[pos] = iteration + 2
                result[pos + 1:] = range(result[pos] + 1,result[pos - 1])
        return result
