class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        present = [r0,c0]
        result = [[r0,c0]]
        totalLeft = R * C - 1
        direction = 1  #1 right,2 down,3 left,4 up
        travelLength = 1    #The length we should travel in this direction
        hasTraveled = 0 #The length we have traveled along this direction
        while totalLeft:
            print(direction)
            if direction == 1:
                present[1] += 1
                if 0 <= present[0] <= R - 1 and 0 <= present[1] <= C - 1:
                    result.append(present[:])
                    totalLeft -= 1
                hasTraveled += 1
                if not travelLength - hasTraveled:
                    direction = 2
                    hasTraveled = 0

            elif direction == 2:
                present[0] += 1
                if 0 <= present[0] <= R - 1 and 0 <= present[1] <= C - 1:
                    result.append(present[:])
                    totalLeft -= 1
                hasTraveled += 1
                if not travelLength - hasTraveled:
                    direction = 3
                    travelLength += 1
                    hasTraveled = 0

            elif direction == 3:
                present[1] -= 1
                if 0 <= present[0] <= R - 1 and 0 <= present[1] <= C - 1:
                    result.append(present[:])
                    totalLeft -= 1
                hasTraveled += 1
                if not travelLength - hasTraveled:
                    direction = 4
                    hasTraveled = 0

            else:
                present[0] -= 1
                if 0 <= present[0] <= R - 1 and 0 <= present[1] <= C - 1:
                    result.append(present[:])
                    totalLeft -= 1
                hasTraveled += 1
                if not travelLength - hasTraveled:
                    direction = 1
                    travelLength += 1
                    hasTraveled = 0
        return result

solution = Solution()
solution.spiralMatrixIII(5,6,1,4)
