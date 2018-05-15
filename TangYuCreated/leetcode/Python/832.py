class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for element in A:
            #first reverse them
            element.reverse()
            for i in range(len(element)):
                if element[i] == 1:
                    element[i] = 0
                else:
                    element[i] = 1
        return A
