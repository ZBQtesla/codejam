class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        #reference[i][j] means the i + 1-combinations resulting in target == j + 1
        reference = [
            [] for i in range(k)
        ]
        for ele in reference:
            for i in range(n):
                ele.append([])
        
        for tar in range(min(n,9)):
            reference[0][tar].append([tar + 1])
            
        for row in range(1,k):
            for column in range(n):
                for biggest in range(9,1,-1):
                    if column - biggest >= 0:
                        for combination in reference[row - 1][column - biggest]:
                            if biggest > combination[-1]:
                                reference[row][column].append(combination + [biggest])
        return reference[k - 1][n - 1]
