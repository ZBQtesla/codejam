class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        listS = list(s)
        reverse = list(reversed(s))
        
        if listS == reverse:
            return True
        
        for i in range(len(listS)): 
            if listS[i] != reverse[i]:
                position = i
                break
        del listS[position]
        del reverse[position]
        
        return listS == listS[::-1] or reverse == reverse[::-1]
