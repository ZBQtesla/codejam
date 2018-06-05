class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        listS = []
        for char in s:
            if char.isalnum():
                listS.append(char.lower())
        return list(reversed(listS)) == listS
