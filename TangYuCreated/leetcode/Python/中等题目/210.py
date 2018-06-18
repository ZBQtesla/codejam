class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        numOfActive = [0] * numCourses
        isActive = [True] * numCourses
        incoming = [set() for i in range(numCourses)]
        for edge in prerequisites:
            numOfActive[edge[0]] += 1
            incoming[edge[1]].add(edge[0])
        result = []
        while True in isActive:
            learn = False
            for course in range(numCourses):
                if isActive[course] and numOfActive[course] == 0:
                    result.append(course)
                    for node in incoming[course]:
                        numOfActive[node] -= 1
                    isActive[course] = False
                    
                    learn = True
            if not learn:
                return []
        return result
