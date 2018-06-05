class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left < right:
            middle = (left + right) // 2
            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle
        return letters[left]
