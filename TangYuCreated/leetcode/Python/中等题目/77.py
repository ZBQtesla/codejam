class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = [
            [i] for i in range(1,n + 1)
        ]
        for iteration in range(k - 1):
            temp = []
            for largest in range(n,0,-1):
                for element in result:
                    if largest > element[-1]:
                        temp.append(element + [largest])
            result = temp
        return result
