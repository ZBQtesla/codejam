class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        dic = {chr(i + ord('a')):widths[i] for i in range(26)}
        row = 1
        column = 0
        width = 100
        for letter in S:
            if width - column < dic[letter]:
                row += 1
                column = dic[letter]
            else:
                column += dic[letter]
        return row,column
