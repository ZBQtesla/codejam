class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for element in cpdomains:
            appearance = int(element.split()[0])
            address = element.split()[1]
            
            if address in dic:
                dic[address] += appearance
            else:
                dic[address] = appearance
            
            for pos in range(len(address)):
                if address[pos] == '.':
                    if address[pos + 1:] in dic:
                        dic[address[pos + 1:]] += appearance
                    else:
                        dic[address[pos + 1:]] = appearance
        result = []
        print(dic)
        for address in dic:
            result.append(' '.join([str(dic[address]),address]))
        
        return result
