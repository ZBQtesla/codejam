class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 1:
            return 1
        if length == 0:
            return 0
        oddPalindrome = [True] * length
        lengthOdd = length
        evenPalindrome = [s[i] == s[i + 1] for i in range(length - 1)]
        result = lengthOdd + evenPalindrome.count(True)
        
        for i in range((lengthOdd - 1) // 2):   #recursive times
            for j in range(lengthOdd - 2 * (i + 1)):
                oddPalindrome[j] = oddPalindrome[j + 1] and s[2 * i + 2 + j] == s[ j]
                if oddPalindrome[j]:
                    result += 1
            #oddPalindrome[-i - 1] = oddPalindrome[-i - 2] = False
            #result += oddPalindrome.count(True)
        
        for i in range((lengthOdd - 2) // 2):
            for j in range(lengthOdd - 1 - 2 * (i + 1)):
                evenPalindrome[j] = evenPalindrome[j + 1] and s[j] == s[j + 2 * i + 3]
                if evenPalindrome[j]:
                    result += 1
            #evenPalindrome[-i - 1] = evenPalindrome[-i - 2] = False
            #result += evenPalindrome.count(True)
            
        return result
