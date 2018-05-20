class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        numsd = 0
        numsu = 0
        numsl = 0
        numsr = 0
        for s in moves:
            if s == 'D':
                numsd += 1
            elif s == 'L':
                numsl += 1
            elif s == 'R':
                numsr += 1
            else:
                numsu += 1
        return numsd == numsu and numsr == numsl
