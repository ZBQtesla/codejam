class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        reference = []
        for word in words:
            temp = 0
            for char in word:
                temp |= 1 << (ord(char) - ord('a'))
            reference.append(temp)
        maxLength = 0
        for first in range(len(reference)):
            for second in range(first,len(reference)):
                if not reference[first] & reference[second]:
                    possible = len(words[first]) * len(words[second])
                    maxLength = possible if possible > maxLength else maxLength
        return maxLength
