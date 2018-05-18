
def numofflip(string,num):
    flipsum = 0
    if '-' not in string:
        return flipsum
    while '-' in string:
        listofstring = list(string)
        left = string.find('-')
        right = string.rfind('-')
        if right - left < num - 1:
            return "IMPOSSIBLE"
        elif right - left == num - 1:
            if string[left:right + 1] == (right - left + 1) * '+':
                return flipsum
            elif string[left:right + 1] == (right - left + 1) * '-':
                return flipsum + 1
            else:
                return "IMPOSSIBLE"
        else:
            for i in range(left,left + num):
                if listofstring[i] == '-':
                    listofstring[i] = '+'
                else:
                    listofstring[i] = '-' #flip a pancake
        flipsum += 1
        auxstring = ''
        for i in listofstring:
            auxstring += i
        string = auxstring

def solve():
    infile = open("A-large-practice.in","r")
    outfile = open("A-large-practice_out.txt","w")
    numofcases = int(infile.readline().strip())
    listofcases = []
    for i in range(numofcases):
        listofcases.append(list(infile.readline().split()))
        listofcases[i][1] = int(listofcases[i][1])  #Get the input in the format:[ ["-+-+-+---",int]...]
    listofoutput = []
    for i in range(numofcases): #this for loop is used to manipulate the i-th item in the listofcases
        listofoutput.append(numofflip(listofcases[i][0],listofcases[i][1]))

    #finish the computation,and print the output to the out file
    for row in range(numofcases):
        outfile.write("Case #"+str(row + 1)+': '+str(listofoutput[row])+'\n')
    #finish the outputing
    infile.close()
    outfile.close()

solve()
