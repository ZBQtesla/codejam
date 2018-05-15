class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        liststr = list(s.split())
        result = ''
        for i in range(len(liststr)):
            liststr[i] = liststr[i][::-1]
        for i in range(len(liststr) - 1):
            liststr[i] += ' '
        for i in range(len(liststr)):
            result += liststr[i]
            
        return result
