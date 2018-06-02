def getInput(infile):
    '''
    :type infile:str
    :return type:list[listofCase[list[A timetable],list[B timetable]]]
    :format timetable:(int(depart),int(arrival))
    '''
    file = open(infile,'r')
    inputList = file.readlines()
    numOfCases = int(inputList.pop(0))
    result = []
    for i in range(numOfCases):
        turnaround = int(inputList.pop(0).strip())
        numOfAtrain = int(inputList[0].split()[0])
        numOfBtrain = int(inputList[0].split()[1])
        del inputList[0]
        result.append([])   #to store case
        result[i].append([])    #to store A timetable
        for j in range(numOfAtrain):
            departTime = changeToMin(inputList[0][:2],inputList[0][3:5])
            arrivalTime = changeToMin(inputList[0][6:8],inputList[0][9:11]) + turnaround
            trip = (departTime,arrivalTime)
            del inputList[0]
            result[i][0].append(trip)

        result[i].append([])    #to store B timetable
        for j in range(numOfBtrain):
            departTime = changeToMin(inputList[0][:2],inputList[0][3:5])
            arrivalTime = changeToMin(inputList[0][6:8],inputList[0][9:11]) + turnaround
            trip = (departTime,arrivalTime)
            del inputList[0]
            result[i][1].append(trip)

    file.close()
    
    return result

def changeToMin(hour,minute):
    '''
    :type hour:str
    :type minute:str
    :return type:integer

    '''
    return 60 * int(hour) + int(minute)

def writeOutput(outfile,outList):
    '''
    :type outfile:str
    :type outList:list[ listOfCase[int,int] ]
    :return type:None

    '''
    file = open(outfile,'w')
    for i in range(len(outList)):
        file.write('Case #' + str(i + 1) + ': ' + str(outList[i][0]) + ' ' + str(outList[i][1]) + '\n')

    file.close()

def arrangeTrain(case):
    '''
    :type case:list[[timetable A],[timetable B]]
    :format timetable:[tuple(trip i)...]
    :return type:tuple(A train,B train)
    '''
    case[0].sort(key = lambda trip:trip[0]) #sorted by the departure time
    case[1].sort(key = lambda trip:trip[0])
    timeTableA = case[0]    #[(time1,time2)]
    timeTableB = case[1]
    
    numOfAtrain = 0
    numOfBtrain = 0

    while timeTableA != [] and timeTableB != []:
        if timeTableA[0][0] < timeTableB[0][0]: #we have to arrange an A train
            numOfAtrain += 1
            arrivalTime = timeTableA[0][1]
            del timeTableA[0]   #This trip has been finished
            useTheTrain(arrivalTime,'B',timeTableA,timeTableB)  #make use of the train
        else:
            numOfBtrain += 1
            arrivalTime = timeTableB[0][1]
            del timeTableB[0]
            useTheTrain(arrivalTime,'A',timeTableA,timeTableB)
    
    if timeTableA != []:
        numOfAtrain += len(timeTableA)
    else:
        numOfBtrain += len(timeTableB)

    return numOfAtrain,numOfBtrain

             
def useTheTrain(arrivalTime,station,timeTableA,timeTableB):
    '''
    :arrivalTime:int
    :station:str,== 'A' or 'B'
    :return type:None
    '''
    
    state = False
    if station == 'A':  #The train arrives at A,at time arrivalTime
        for i in range(len(timeTableA)): #type trip:tuple(int,int)
            if timeTableA[i][0] >= arrivalTime:
                arrival = timeTableA[i][1]
                del timeTableA[i]
                state = True    #we have altered the timeTable
                break
        if state:
            useTheTrain(arrival,'B',timeTableA,timeTableB)
    else:
        for i in range(len(timeTableB)):
            if timeTableB[i][0] >= arrivalTime:
                arrival = timeTableB[i][1]
                del timeTableB[i]
                state = True
                break
        if state:
            useTheTrain(arrival,'A',timeTableA,timeTableB)


def main():
    inputList = getInput("B-large-practice.in")

    result = []
    for case in inputList:
        result.append(arrangeTrain(case))

    writeOutput("solve_B-large-practice.txt",result)

main()
    




