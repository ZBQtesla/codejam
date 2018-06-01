def getInput(infile):
    file = open(infile,'r')
    listOfInput = file.readlines()
    
    listOfInput[0] = int(listOfInput[0].strip())
    for i in range(1,len(listOfInput)):
        listOfInput[i] = listOfInput[i].split()
    for i in range(1,len(listOfInput)):
        listOfInput[i][0] = int(listOfInput[i][0])
        listOfInput[i][1] = int(listOfInput[i][1])
    return listOfInput
    #ListOfInput == [N,[4,2],[5,2]...)

def writeOutput(outfile,outlist):
    #outlist == [[1,0],[2,0]...)
    file = open(outfile,'w')
    for i in range(len(outlist)):
        file.write('Case #' + str(i + 1) + ': ' + str(outlist[i][0]) + ' ' + str(outlist[i][1]) + '\n') 
    file.close()

def compute(N,K):
    '''
    :type N:int
    :type K:int
    :return type:list[int]
    '''
    result = []
       
    if N == 0:
        return [0,0]
    if N == 1:
        return [0,0]
    if N == 2 and K == 2:
        return [0,0]
    if K == 1:
        middle = (N - 1) // 2
        smallSize = middle
        largeSize = N - smallSize - 1
        return [largeSize,smallSize]

    dic = {'largeSize':N,'largeNum':1,'smallSize':N,'smallNum':0}
    while K > dic['largeNum'] + dic['smallNum']:
        K -= dic['smallNum'] + dic['largeNum']

        oplarge = compute(dic['largeSize'],1)
        opsmall = compute(dic['smallSize'],1)
        templargeNum = dic['largeNum']
        tempsmallNum = dic['smallNum']

        #the four variables are used to store the size of different-sized intervals
        maxoflarge = max(oplarge)
        minoflarge = min(oplarge)
        maxofsmall = max(opsmall)
        minofsmall = min(opsmall)

        dic['largeSize'] = maxoflarge
        dic['smallSize'] = minofsmall

        dic['largeNum'] = 0
        dic['smallNum'] = 0

        dic['largeNum'] += templargeNum
        dic['smallNum'] += tempsmallNum

        if maxofsmall == maxoflarge:
            dic['largeNum'] += tempsmallNum
        else:
            dic['smallNum'] += tempsmallNum

        if maxoflarge == minoflarge:
            dic['largeNum'] += templargeNum
        else:
            dic['smallNum'] += templargeNum

        if dic['smallSize'] == 0:
            dic['smallNum'] = 0

    if K > dic['largeNum']:
        return compute(dic['smallSize'],1)
    else:
        return compute(dic['largeSize'],1)

def main():
    inputList = getInput("C-large-practice.in")

    numOfCases = inputList.pop(0)
    outList = []
    
    for i in range(numOfCases):
        outList.append(compute(inputList[i][0],inputList[i][1]))

    writeOutput("solve_C-large-practice.txt",outList)

main()
    

        
















        
