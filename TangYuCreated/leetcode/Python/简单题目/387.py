class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        reference = {}
        for index in range(len(s)):
            if s[index] in reference:
                reference[s[index]] = -1
            else:
                reference[s[index]] = index
        unique = [reference[key] for key in reference if reference[key] != -1]
        return min(unique) if unique else -1
