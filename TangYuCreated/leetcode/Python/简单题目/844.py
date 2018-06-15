class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        listS = []
        for char in S:
            if char != '#':
                listS.append(char)
            else:
                if listS:
                    del listS[-1]
        listT = []
        for char in T:
            if char != '#':
                listT.append(char)
            else:
                if listT:
                    del listT[-1]
        return listS == listT
