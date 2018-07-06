class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        sumP = 0
        length = len(S)
        if length == 2:
            return 1
        for i in range(length):
            if S[i] == '(':
                sumP += 1
            else:
                sumP -= 1
                if sumP == 0:
                    if i == length - 1:
                        return 2 * self.scoreOfParentheses(S[1:-1])
                    else:
                        return self.scoreOfParentheses(S[:i + 1]) + self.scoreOfParentheses(S[i + 1:])
