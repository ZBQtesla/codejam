class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic ={'2':set('abc'),'3':set('def'),'4':set('ghi'),'5':set('jkl'),'6':set('mno'),'7':set('pqrs'),'8':set('tuv'),'9':set('wxyz')}
        res = ['']
        for n in digits:
            res = [i+j for i in res for j in dic[n]]
        return res
