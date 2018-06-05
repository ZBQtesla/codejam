def getInput(infile):
    file = open(infile,'r')

    inputList = file.readlines()
    for i in range(len(inputList)):
        inputList[i] = int(inputList[i].strip())

    del inputList[0]
    file.close()

    return inputList

def writeOutput(outfile,result):
    # Caution!the element in result is strings
    file = open(outfile,'w')

    for i in range(len(result)):
        file.write('Case #'+str(i + 1)+': '+result[i]+'\n')
    file.close()

def theLastInteger(n):
    if n == 0:
        return 'INSOMNIA'
    remaining = set(range(10))
    factor = 1
    while remaining:
        integer = n * factor
        digits = decompose(integer)
        remaining -= digits

        factor += 1
    return str(integer)

def decompose(num):
    result = set()
    while num != 0:
        result.add(num % 10)
        num //= 10
    return result

def main():
    inputList = getInput('A-large-practice.in')

    output = []
    for i in range(len(inputList)):
        output.append(theLastInteger(inputList[i]))

    writeOutput('solve_A-large-practice.txt',output)

main()
