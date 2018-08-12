class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        #a is the number of five-dollar bills
        #b is the number of ten-dollar bills
        a = b = 0
        for bill in bills:
            if bill == 5 :
                a += 1
            elif bill == 10:
                b += 1
                a -= 1
            else:
                if b == 0:
                    a -= 3
                else:
                    b -= 1
                    a -= 1
            
            if a < 0:
                return False
        return True
