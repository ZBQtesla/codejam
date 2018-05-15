class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        listx = []
        listy = []
        length = 32
        for i in range(length):
            listx.insert(0,x % 2)
            x //= 2
        for z in range(length):
            listy.insert(0,y % 2)
            y //= 2
        sum = 0
        
        for p in range(length):
            if listx[p] != listy[p]:
                sum += 1
                
        return sum
            
