class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic ={'2':set('abc'),'3':set('def'),'4':set('ghi'),'5':set('jkl'),'6':set('mno'),'7':set('pqrs'),'8':set('tuv'),'9':set('wxyz')}
        result = []
        def generate(digits,string):
            if len(digits) == 1:
                for letter in dic[digits]:
                    result.append(string + letter)
            else:
                for letter in dic[digits[0]]:
                    generate(digits[1:],string + letter)
        generate(digits,'')
        return result
