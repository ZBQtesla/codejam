class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        numOfPerson = len(M)
        discovered = numOfPerson * [False]
        result = 0
        for i in range(numOfPerson):
            if not discovered[i]:
                discovered[i] = True
                result += 1
                
                friends = [j for j in range(numOfPerson) if M[i][j]]
                length = len(friends)
                finished = 1
                while finished < length:
                    focus = friends[finished]
                    discovered[focus] = True
                    
                    for j in range(numOfPerson):
                        if M[focus][j] and j not in friends:
                            friends.append(j)
                            length += 1
                    finished += 1
        return result
