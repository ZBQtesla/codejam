class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lengthA = len(A)
        lengthB = len(B)
        if lengthA != lengthB:
            return False
        different = []
        for i in range(lengthA):
            if A[i] != B[i]:
                different.append(i)
        lengthD = len(different)
        if not different:
            reference = dict()
            for i in range(lengthA):
                if A[i] == B[i]:
                    if A[i] not in reference:
                        reference[A[i]] = True
                    else:
                        return True
            return False
        if lengthD >= 3 or lengthD == 1:
            return False
        first,second = different[0],different[1]
        if [A[first],A[second]] == [B[second],B[first]]:
            return True
        else:
            return False
