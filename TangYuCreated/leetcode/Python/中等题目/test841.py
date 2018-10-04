class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        present = set([0])
        left = len(rooms) - 1
        discovered = set([0])
        while left:
            print(present)
            print(discovered)
            print()
            if not present:
                return False
            nextLayer = set()
            for room in present:
                for key in rooms[room]:
                    if not key in discovered:
                        nextLayer.add(key)
                        left -= 1
            present = nextLayer
        return True

solution = Solution()
solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
