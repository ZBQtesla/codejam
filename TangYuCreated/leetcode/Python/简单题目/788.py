class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        dic = ['0','1','2','5','6','8','9']
        length = len(str(N))
        reference = [0 for i in range(length)]
        string = '0' * length
        
        result = 0
        stringN = str(N)
        
        while string <= stringN:
            if '2' in string or '5' in string or '6' in string or '9' in string:
                result += 1
            
            for i in range(length - 1,-1,-1):
                if reference[i] == 6:
                    if i:
                        reference[i] = 0
                    else:
                        return result
                else:
                    reference[i] += 1
                    break
            
            string = ''.join([dic[i] for i in reference])
        
        return result
