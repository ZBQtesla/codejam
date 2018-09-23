class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        dic = {}
        previous = A[0]
        currentLength = 0
        difference = A[1] - A[0]
        
        for num in A[1:]:
            if num - previous == difference:
                currentLength += 1
            else:
                if currentLength in dic:
                    dic[currentLength] += 1
                else:
                    dic[currentLength] = 1
                difference = num - previous
                currentLength = 1
            previous = num
        if currentLength in dic:
            dic[currentLength] += 1
        else:
            dic[currentLength] = 1
        result = 0
        for length in dic:
            result += dic[length] * (length - 1) * (length) // 2
        return result
