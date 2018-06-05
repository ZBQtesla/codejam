def getInput(infile):
    file = open(infile,'r')
    inputList = file.readlines()
    del inputList[0]
    for i in range(len(inputList)):
        inputList[i] = inputList[i].strip()
    file.close()

    return inputList

def writeOutput(outfile,output):
    file = open(outfile,'w')
    for i in range(len(output)):
        file.write('Case #'+str(i + 1)+': '+str(output[i]) + '\n')
    file.close()

def compute(pattern):
    if pattern == len(pattern) * '+':
        return 0
    
