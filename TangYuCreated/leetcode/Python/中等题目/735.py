class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        while len(asteroids):
            num = len(asteroids)
            explode = []
            for left in range(num - 1):
                if asteroids[left] > 0 and asteroids[left + 1] < 0:
                    leftMass = abs(asteroids[left])
                    rightMass = abs(asteroids[left + 1])
                    if leftMass > rightMass:
                        explode.append(left + 1)
                    elif rightMass > leftMass:
                        explode.append(left)
                    else:
                        explode.append(left)
                        explode.append(left + 1)
            if not explode:
                return asteroids
            else:
                for planet in reversed(explode):
                    del asteroids[planet]
        return asteroids
