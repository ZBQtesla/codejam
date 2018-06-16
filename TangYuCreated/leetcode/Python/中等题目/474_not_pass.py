class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        reference = []
        result = 0
        for row in range(m + 1):
            reference.append([])
        for List in reference:
            for col in range(n + 1):
                List.append([0])
        
        for num0 in range(m + 1):
            for num1 in range(n + 1):
                for i in range(len(strs)):
                    temp0 = strs[i].count('0')
                    temp1 = len(strs[i]) - temp0
                    
                    if num0 >= temp0 and num1 >= temp1:
                        optimal = max(1 + reference[num0 - temp0][num1 - temp1][i],reference[num0][num1][-1]) 
                    else:
                        optimal = reference[num0][num1][-1]
                    
                    reference[num0][num1].append(optimal)
                    
            result = max(max(reference[num0][num1]),result)
        return result
