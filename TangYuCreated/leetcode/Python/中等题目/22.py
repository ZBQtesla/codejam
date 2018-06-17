class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return ''
        result = []
        
        def helper(numLeft,numRight,already):
            if not numLeft:
                result.append(already + ')' * numRight)
            elif numLeft == numRight:
                helper(numLeft - 1,numRight,already + '(')
            else:
                helper(numLeft - 1,numRight,already + '(')
                helper(numLeft,numRight - 1,already + ')')
        helper(n,n,'')
        return result
