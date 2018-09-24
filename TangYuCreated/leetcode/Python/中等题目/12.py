class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        ref = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        while num:
            for element in ref:
                if num >= element[0]:
                    result.append(element[1])
                    num -= element[0]
                    break
        return ''.join(result)
