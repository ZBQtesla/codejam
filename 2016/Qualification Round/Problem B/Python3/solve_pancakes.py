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
    lastneg = pattern.rfind('-')
    pattern = pattern[:lastneg + 1]
    if pattern.startswith('+'):
        for i in range(0,len(pattern)):
            if pattern[i] != '+':
                position = i
                break
        return compute((position) * '-' + pattern[position:]) + 1
    else:
        return compute(neg(pattern[::-1])) + 1

def neg(string):
    listS = list(string)
    for i in range(len(listS)):
        listS[i] = '-' if listS[i] == '+' else '+'
    return ''.join(listS)

def main():
    inputList = getInput('B-large-practice.in')

    output = []
    for element in inputList:
        output.append(compute(element))

    writeOutput('solve_B-large-practice.txt',output)

main()
