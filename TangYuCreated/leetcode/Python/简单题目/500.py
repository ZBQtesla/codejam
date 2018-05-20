class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        listofrows = [
            list('QWERTYUIOPqwertyuiop'),
            list('ASDFGHJKLasdfghjkl'),
            list('ZXCVBNMzxcvbnm')
        ]
        result = []
        for word in words:
            state = True
            for row in range(3):
                if word[0] in listofrows[row]:
                    target = row
                    break
            for element in word:
                if element not in listofrows[target]:
                    state = False
                    break
            if state == True :
                result.append(word)
                
        return result
