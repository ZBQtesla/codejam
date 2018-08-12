class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        result = [0]
        if length == 1:
            return result
        reference = dict()
        reference[temperatures[-1]] = length - 1
        for i in range(length - 2,-1,-1):
            temp = [reference[tem] for tem in reference if tem > temperatures[i]]
            if temp:
                result.append(min(temp) - i)
            else:
                result.append(0)
            reference[temperatures[i]] = i
        return list(reversed(result))
