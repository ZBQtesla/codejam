def getInput(infile):
    '''
    :type infile:file
    :return type:list[listofCase[list[A timetable],list[B timetable]]]
    :format timetable:(int(depart),int(arrival))
    '''
    file = open(infile,'r')
    inputList = file.readlines()
    numOfCases = int(inputList.pop(0))
    result = []
    for i in range(numOfCases):
        turnaround = int(inputList.pop(0).strip())
        numOfAtrain = int(inputList[0][0].strip())
        numOfBtrain = int(inputList[0][2].strip())
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

inputList = getInput("B-small-practice.in")
print(inputList)
    
        
            
