class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        if g == [] or s == []:
            return 0
        count = 0
        while g != [] and s != []:
            if g[0] <= s[0]:
                count += 1
                del g[0]
                del s[0]
            else:
                del s[0]
        return count
