class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        isneg = True if numerator * denominator < 0 else False
        numerator,denominator = abs(numerator),abs(denominator)
        string = str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return string if not isneg else '-' + string
        
        string += '.'
        decimal = ''
        remainders = []
        
        numerator *= 10
        remainders.append(numerator)
        while numerator != 0 and numerator not in remainders[:-1]:
            quotient,numerator = divmod(numerator,denominator)
            decimal += str(quotient)
            
            numerator *= 10
            remainders.append(numerator)
            
        if numerator == 0:
            return string + decimal if not isneg else '-' + string + decimal
        else:
            result = string + decimal[:remainders.index(numerator)] + '(' + decimal[remainders.index(numerator):] + ')'
            return result if not isneg else '-' + result
            
