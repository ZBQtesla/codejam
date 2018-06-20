class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        reference = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        special = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        index = 0
        length = len(s)
        count = 0
        while index <= length - 1:
            if s[index:index + 2] in special:
                count += special[s[index:index + 2]]
                index += 2
            else:
                count += reference[s[index]]
                index += 1
        return count
