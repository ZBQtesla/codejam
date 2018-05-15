class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        #We use an array ,result[] here to be the teturn value
        #And use count[] here to know the position of those 0's in result[]
        #Then we use this information to manipulate the string
        result = []
        count = []
        for i in range(len(S)):
            result.append(-1)
        for i in range(len(S)):
            if S[i] == C:
                result[i] = 0
                count.append(i)
        nowr = 0
        left = count[nowr]
        #now we begin the first recursion
        for i in range(left +1):
            result[i] = left - i
            
        if len(count) == 1:
            for i in range(left,len(result)):
                result[i] = i - left
        lencount = len(count)        
        while -1 in result and nowr != lencount - 1:
            right = count[nowr + 1]
            left = count[nowr]
            nowr += 1
            for i in range(left,right + 1):
                result[i] = i - left if i - left < right - i else right - i
        if -1 in result:
            last = count[nowr]
            for i in range(last,len(result)):
                result[i] = i - last
        return result
