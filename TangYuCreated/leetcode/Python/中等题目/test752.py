class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        presentRoot = ['0000']  #The present layer
        presentDesti = [target]
        rootDiscover = deadends[:]  #The upper layer of our present layer
        destiDiscover = deadends[:]
        rootDepth = destiDepth = 0
        while presentRoot and presentDesti:
            nextRoot = []
            hasDiscoveredRoot = rootDiscover + presentRoot
            for node in presentRoot:
                for pos in range(4):
                    element1 = node[:pos] + chr((ord(node[pos]) - ord('0') - 1) % 10 + ord('0')) + node[pos + 1:]
                    element2 = node[:pos] + chr((ord(node[pos]) - ord('0') + 1) % 10 + ord('0')) + node[pos + 1:]
                    if element1 not in hasDiscoveredRoot:
                        nextRoot.append(element1)
                        hasDiscoveredRoot.append(element1)
                    if element2 not in hasDiscoveredRoot:
                        nextRoot.append(element2)
                        hasDiscoveredRoot.append(element2)
            rootDiscover,presentRoot = presentRoot + deadends,nextRoot
            rootDepth += 1
            for element in presentRoot:
                if element in presentDesti:
                    print(rootDepth + destiDepth)
                    return rootDepth + destiDepth
            
            nextDesti = []
            hasDiscoveredDesti = destiDiscover + presentDesti
            for node in presentDesti:
                for pos in range(4):
                    element1 = node[:pos] + chr((ord(node[pos]) - ord('0') - 1) % 10 + ord('0')) + node[pos + 1:]
                    element2 = node[:pos] + chr((ord(node[pos]) - ord('0') + 1) % 10 + ord('0')) + node[pos + 1:]
                    if element1 not in hasDiscoveredDesti:
                        nextDesti.append(element1)
                        hasDiscoveredDesti.append(element1)
                    if element2 not in hasDiscoveredDesti:
                        nextDesti.append(element2)
                        hasDiscoveredDesti.append(element2)
            destiDiscover,presentDesti = presentDesti + deadends,nextDesti
            destiDepth += 1
            for element in presentDesti:
                if element in presentRoot:
                    print(rootDepth + destiDepth)
                    return rootDepth + destiDepth
        else:
            print(-1)
            return -1

solution = Solution()
solution.openLock(["6776","7686","7686","8666","7788","8868","6667","8776","7688","7687","6668","7687","7776","6867","8788","8787","8886","7668","6678","6766","8677","7778","6886","8766","7768","8686","7788","7767","7786","6778","7686","6778","8778","7887","8876","7666","8766","6667","7877","7778","7868","8886","6868","6887","7667","8887","8687","8668","6678","7886","7686","7887","7686","8767","8676","8668","7666","8867","6788","6868","6778","6866","8787","8877","7667","6766","7778","8878","6786","7677","7668","7676","6876","6868","8666","8768","8768","6786","8677","6788","8788","7876","8788","8876","7787","6778","8887","6767","6788","8778","6887","6876","6677","8667","7686","6877","7866","6668","7786","7766","8786","8877","8877","6778","7786","7687","8766","6776","8666","8667","6767","7878","6776","6776","7888","6868","8788","6668","7768","8778","6676","6678","6877","8886","8876","8687","6686","7877","6868","7876","8767","6766","6666","8666","6788","6686","8666","6866","6677","8688","7676","8676","8668","8676","8768","6886","8668","6767","6788","6887","6868","7676","6777","6778","6678","8686","6887","8687","7786","8878","6878","8866","6886","6678","6777","7666","6788","6878","6867","6877","6776","8668","8888","8768","6677","8877","7676","6777","6688","6887","6778","8877","6766","6778","6766","6787","6788","8788","7687","7766","8876","8766","8876","7686","8676","7686","6866","7666","6878","7888","6878","7866","7677","6776","8877","7767","6786","7676","6886","7886","8886","6676","6668","8768","8776","8788","7767","7867","7687","6687","8688","7887","8767","6867","7867","7768","6877","6686","8788","6887","8788","6866","8886","8678","7786","7667","6787","8667","7888","8676","7778","7676","8786","7768","7676","7876","6788","8766","8687","8668","6667","8686","8667","8888","6677","8776","7786","8667","8777","7866","6868","8867","7787","8687","6666","7667","7788","6876","6866","8686","8786","6777","6667","6676","8887","8786","8667","7676","6867","8666","8677","7878","7866","7666","6686","8688","6678","6788","8787","7768","6788","6686","7887","6668","8677","7887","6678","6787","8868","7766","8668","8666","8766","7686","6676","6778","7788","8678","8877","6868","7877","6687","6668","6877","7868","8667","6767","7777","6877","8768","7886","7777","8778","8867","6876","6688","8888","6867","8877","8776","7888","8687","6868","7887","8888","7668","8867","6867","8888","8667","6878","8768","6876","7676","8866","6666","7778","7676","7688","6686","8676","8788","8777","7876","8877","8686","8688","7768","8686","8767","8887","6868","7676","8676","8778","8876","6876","8677","8886","8866","6788","7766","7867","7888","7668","8678","6787","6786","6667","7677","8688","6678","6767","7787","6778","6687","8667","8666","6778","6776","8876","8878","7668","8768","6678","8677","7776","6878","8677","6866","6666","6668","6778","6887","6877","7868","8687","8688","7877","6686","6686","6886","6886","7888","6668","7787","6876","7878","8788","7866","8777","8888","7886","8766","8878","6887","6776","7667","8788","7876","8678","7668","6786","6866","7776","7676","6676","7766","6776","6668","8687","7668","7677","8768","7787","6678","6767","6878","6778","6787","6868","6876","7688","6668","6877","8778","7677","7686","6876","7866","8668","8868","7668","8678","8687","7677","6888","7876","7687","6888","7788","6767","6866","8776","8887","6778","7768","6868","8677","7686","8888","7868","6688","6788","6686","8667","7766","8867","6867","7866","8688","7786","7677","6788","7887","6888","6787","8867","6667","6778"],"7678")

