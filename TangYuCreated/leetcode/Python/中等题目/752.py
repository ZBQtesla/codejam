class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        presentRoot = {'0000'}  #The present layer
        presentDesti = {target}
        rootDiscover = deadends.copy()  #The upper layer of our present layer
        destiDiscover = deadends.copy()
        rootDepth = destiDepth = 0
        while presentRoot and presentDesti:
            nextRoot = set()
            hasDiscoveredRoot = rootDiscover | presentRoot
            for node in presentRoot:
                for pos in range(4):
                    element1 = node[:pos] + chr((ord(node[pos]) - ord('0') - 1) % 10 + ord('0')) + node[pos + 1:]
                    element2 = node[:pos] + chr((ord(node[pos]) - ord('0') + 1) % 10 + ord('0')) + node[pos + 1:]
                    if element1 not in hasDiscoveredRoot:
                        nextRoot.add(element1)
                        hasDiscoveredRoot.add(element1)
                    if element2 not in hasDiscoveredRoot:
                        nextRoot.add(element2)
                        hasDiscoveredRoot.add(element2)
            rootDiscover,presentRoot = presentRoot | deadends,nextRoot
            rootDepth += 1
            for element in presentRoot:
                if element in presentDesti:
                    return rootDepth + destiDepth
            
            nextDesti = set()
            hasDiscoveredDesti = destiDiscover | presentDesti
            for node in presentDesti:
                for pos in range(4):
                    element1 = node[:pos] + chr((ord(node[pos]) - ord('0') - 1) % 10 + ord('0')) + node[pos + 1:]
                    element2 = node[:pos] + chr((ord(node[pos]) - ord('0') + 1) % 10 + ord('0')) + node[pos + 1:]
                    if element1 not in hasDiscoveredDesti:
                        nextDesti.add(element1)
                        hasDiscoveredDesti.add(element1)
                    if element2 not in hasDiscoveredDesti:
                        nextDesti.add(element2)
                        hasDiscoveredDesti.add(element2)
            destiDiscover,presentDesti = presentDesti | deadends,nextDesti
            destiDepth += 1
            for element in presentDesti:
                if element in presentRoot:
                    return rootDepth + destiDepth
        else:
            return -1
