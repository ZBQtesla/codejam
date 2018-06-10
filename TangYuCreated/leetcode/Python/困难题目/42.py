class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        highest = max(height)
        left = height[0]
        i = 1
        volume = 0
        leftPosition = 0
        length = len(height)
        while left <= highest and i <= length - 1:
            if height[i] >= left:
                volume += left * (i - leftPosition - 1) - sum(height[leftPosition + 1:i])
                left = height[i]
                leftPosition = i
            i += 1
        right = height[-1]
        rightPosition = length - 1
        i = rightPosition - 1
        while right < highest and i >= 0:
            if height[i] >= right:
                volume += right * (rightPosition - i - 1) - sum(height[rightPosition - 1:i:-1])
                right = height[i]
                rightPosition = i
            i -= 1
        return volume
