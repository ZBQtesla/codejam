class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        currentVal = 1
        currentLower = 0
        result = []
        n = rowIndex
        num = rowIndex + 1
        while currentLower <= n // 2:
            result.append(currentVal)
            currentLower += 1
            currentVal = currentVal * (n - currentLower + 1) // currentLower
        result.extend(result[num // 2 - 1::-1])
        return result
