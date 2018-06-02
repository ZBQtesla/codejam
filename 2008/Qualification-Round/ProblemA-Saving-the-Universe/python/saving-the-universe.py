def getInput(infile):
    '''
    :type infile:file
    :return type:list[list[tuple()]],where each inner tuple is one test scenario
    [ [(engines...)(queries)].....]

    '''
    file = open(infile,'r')
    inputList = file.readlines()
    for i in range(len(inputList)):
        inputList[i] = inputList[i].strip()
    numOfCases = int(inputList.pop(0))
    result = []
    for i in range(numOfCases):
        result.append([])
    while inputList != []:
        indicator = int(inputList.pop(0))
        temptuple = tuple(inputList[:indicator])
        for i in range(indicator):
            inputList.pop(0)
        for i in range(len(result)):
            if len(result[i]) < 2:
                result[i].append(temptuple)
                break
    file.close()
    return result

def writeOutput(outfile,outList):
    '''
    :type outfile:file
    :type outList:list[int]

    '''
    file = open(outfile,'w')
    for i in range(len(outList)):
        file.write('Case #' + str(i + 1) + ': '+ str(outList[i]) + '\n')
    file.close()

def farthestFuture(scenario):
    '''
    :type scenario:list[(engines),(queries)]
    :return type:int  (The number of minimal misses)

    '''
    engines = scenario[0]
    queries = scenario[1]
    currentCache = []
    #print("The initial query is:",queries,'\n' * 3)
    #print("Engines are:",engines,'\n' * 3)
    #To get the initial cache
    while len(currentCache) < len(engines) - 1 and queries != ():
        if queries[0] not in currentCache:
            currentCache.append(queries[0])
        queries = queries[1:]
        #print("Now the queries are:",queries)
        #print("Now the Cache is:",currentCache)
    if queries == ():
        return 0
    count = 0
    #print()
    #print()
    #print()
    while queries != ():
        #print("now the queries are:",queries)
        if queries[0] not in currentCache:
            evictSomeone(currentCache,queries,queries[0])
            count += 1
            #print("now count is:",count)
            #print("now Cache is:",currentCache)
        queries = queries[1:]

    return count


def evictSomeone(currentCache,log,target):
    '''
    :type cunrrentCache:list[str]
    :type log:tuple(str)
    :return type:None

    '''
    farthestUsed = -1
    for i in range(len(currentCache)):
        try:
            if log.index(currentCache[i]) > farthestUsed:
                farthestUsed = log.index(currentCache[i])
                toBeReplaced = i
        except: #the element not in tuple
            currentCache[i] = target
            return None
    currentCache[toBeReplaced] = target

def main():
    inputList = getInput("A-small-practice.in")
    outputList = []
    for i in range(len(inputList)):
        outputList.append(farthestFuture(inputList[i]))

    writeOutput("solve_A-small-practice.txt",outputList)


main()
