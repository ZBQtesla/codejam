class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countS = {}
        countT = {}
        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        for char in countT:
            if char not in countS or countT[char] !=countS[char]:
                return char
