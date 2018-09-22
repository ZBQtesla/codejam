class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0,0)
        flowerbed.insert(len(flowerbed),0)
        result = 0
        
        for pos in range(1,len(flowerbed) - 1):
            if not flowerbed[pos] and not flowerbed[pos - 1] and not flowerbed[pos + 1]:
                result += 1
                flowerbed[pos] = 1
            
        return result >= n
