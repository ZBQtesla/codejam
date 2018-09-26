class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        listS = list(S)
        letters = [[chr(ord('a') + i),0] for i in range(26)]
        result = []
        for char in T:
            letters[ord(char) - ord('a')][1] += 1
        for char in listS:
            result.append(letters[ord(char) - ord('a')][1] * char)
            letters[ord(char) - ord('a')][1] = 0
        for element in letters:
            result.append(element[1] * element[0])
        return ''.join(result)
