class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right + 1):
            listofbiti = self.listofbits(i)
            state = True
            if 0 in listofbiti:
                continue
            for divisor in listofbiti:
                if i % divisor != 0:
                    state = False
                    break
            if state == True:
                result.append(i)
        return result
    def listofbits(self,num):
        listofb = []
        while num != 0:
            h = num % 10
            if h not in listofb:
                listofb.append(h)
            num //= 10
        return listofb
