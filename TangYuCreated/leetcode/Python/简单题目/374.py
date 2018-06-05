# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        guessnum = (left + right) // 2
        while guess(guessnum):
            if guess(guessnum) > 0:
                left = guessnum + 1
            else:
                right = guessnum - 1
            guessnum = (left + right) // 2
        return guessnum
