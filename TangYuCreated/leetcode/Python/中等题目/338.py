class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        current = [0,1]
        length = 2
        while num > length * 2 - 1:
            current.extend([1 + val for val in current])
            length *= 2
        current.extend([1 + val for val in current[:num + 1 - length]])
        return current
