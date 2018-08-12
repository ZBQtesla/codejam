class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        matched = len(s)
        for char in reversed(t):
            if char == s[matched - 1]:
                matched -= 1
            if matched == 0:
                return True
        return False
