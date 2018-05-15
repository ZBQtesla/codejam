class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        listmors = []
        for word in words:
            wordmors =''
            for char in word:
                wordmors += mors[ord(char) - ord('a')]
                
            if wordmors not in listmors:
                listmors.append(wordmors)
                
        return len(listmors)
