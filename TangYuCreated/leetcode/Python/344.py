class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lists = list(s)
        lists.reverse()
        result = ''
        for i in lists:
            result += i
        return result
