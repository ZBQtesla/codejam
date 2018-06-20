class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brace = bracket = parenthesis = 0
        stack = []
        for char in s:
            if char == '(':
                parenthesis += 1
                stack.append(')')
            elif char == ')':
                parenthesis -= 1
                if stack and char != stack.pop():
                    return False
            elif char == '[':
                bracket += 1
                stack.append(']')
            elif char == ']':
                bracket -= 1
                if stack and char != stack.pop():
                    return False
            elif char =='{':
                brace += 1
                stack.append('}')
            elif char == '}':
                brace -= 1
                if stack and char != stack.pop():
                    return False
            
            if parenthesis < 0 or brace < 0 or bracket < 0 :
                return False
        return True if parenthesis == brace == bracket == 0 else False
