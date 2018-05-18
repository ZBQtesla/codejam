def main():
    infile = open("B-large-practice.in","r")
    outfile = open("B_large_output.txt","w")
    listofinteger = []  #used to store the integers,[int]
    getinput(infile,listofinteger)


    listoftidynum = []
    for integer in listofinteger:
        listoftidynum.append(biggesttidy(integer))


    printresult(listoftidynum,outfile)

    infile.close()
    outfile.close()


def getinput(infile,listofinteger):
    '''type (infile):file
        listofstring:list[str]
        return type:int
    '''
    #numofcases is the return value
    numofcases = int(infile.readline().strip())
    for i in range(numofcases):
        listofinteger.append(int(infile.readline().strip()))


def printresult(listoftidynum,outfile):
    '''type listoftidynum:list[integer]
        outfile:file
        '''
    for i in range(len(listoftidynum)):
        outfile.write("Case #" + str(i + 1) + ': ' + str(listoftidynum[i])+'\n')

def biggesttidy(integer):
    '''
        type integer:int
        type string:str
        return type:int = int(string)
    '''

    string = str(integer)
    length = len(string)
    leng = length
    if length == 1:
        return integer
    result = ''

    #real computation
    if string.startswith("1") and "0" in string:    #11111cannot happen
        return int('9' * (length - 1))
    else:   #we can construct a tidy integer of the same exact length
        for i in range(length):
            if not isatidystart(string[i:],string[i]):
                 result += (str(int(string[i]) - 1) + '9' * (leng - 1))
                 break
            else:
                result += string[i]
                leng -= 1
    return int(result)

def isatidystart(string,charint):
    length = len(string)
    return  int(length * charint) <= int(string) 
            

main()













    
