class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        aux = set(list(S))
        reference = {}
        for char in aux:
            reference[char] = S.rfind(char)
        
        leftEnd = 0
        rightEnd = reference[S[0]]
        
        result = []
        for i in range(len(S)):
            rightEnd = max(rightEnd,reference[S[i]])
            if i == rightEnd:
                result.append(rightEnd - leftEnd + 1)
                leftEnd = rightEnd + 1
        return result
