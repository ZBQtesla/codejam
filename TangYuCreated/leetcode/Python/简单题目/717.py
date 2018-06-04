class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
        while len(bits) > 1:
            if bits[0] == 0:
                del bits[0]
            else:
                del bits[:2]
        if len(bits) == 0:
            return False
        else:
            return True
