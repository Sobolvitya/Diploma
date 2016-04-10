import Main
import random
import itertools
possibleD = [-1,0,1]
arrayOfPossibleDLines = []
generalD = []

def findPossibleDString (sum, ArrD,count,Aconcret,sumTrue,generalD):
   #this func find possible string for dependency matrix, for concret line
   #sum - sum of components multiplay weighth
   #ArrD - array for possible relationships values
   #count - number of current iteration (what component now we use)
   #AConcret - current Ai for build dependency matrix
   #sumTrue - (-1,0,1), this is possible value for sum, use Main.thereholds
   #generalD - array for right array of dependecyMatrix

    if Main.countComp == count:
        if sumTrue == 1:
            if sum > Main.thereholds:
               generalD.append(ArrD)
        if sumTrue == 0:
            if sum >= -Main.thereholds and sum <= Main.thereholds:
                generalD.append(ArrD)
        if sumTrue == -1:
            if sum < -Main.thereholds:
                 generalD.append(ArrD)
        return
    for i in possibleD:
        sumTmp = sum +  Aconcret[count] * i
        countTmp = count + 1
        tmpArrD = []
        for j in ArrD:
            tmpArrD.append(j)
        tmpArrD.append(i)
        findPossibleDString(sumTmp,tmpArrD,countTmp,Aconcret,sumTrue,generalD)
        #print ("Exit")


def findDependMatrix (A1, A2):
    for i in range(len(A1)):
        diff = A2[i] - A1[i]
        ArrD = []
        generalDForString = []
        global generalD
        if diff == 0 and A2[i] == 1:
            findPossibleDString(0,ArrD,0,A1,-1,generalDForString)

        if diff == 0 and A2[i] == Main.KState:
            findPossibleDString(0,ArrD,0,A1,1,generalDForString)


        findPossibleDString(0,ArrD,0,A1,diff,generalDForString)
        generalD.append(generalDForString)


def getNextVarietyOfDependecyMatrix():
    for i in range (len(sequenceCombinationDependMatrix)-1,-1,-1):
        if (sequenceCombinationDependMatrix[i] + 1 <= lastElement[i]):
            sequenceCombinationDependMatrix[i] += 1
            return True
        else:
            sequenceCombinationDependMatrix[i] = 0
    return False

def setFisrtAndLastElementSequens():
    '''
    We use sequens from 0...0 to N...N to use different
    combination of dependecy matrix, where N is the last number of
    every possible combinations
    '''
    global lastElement
    lastElement = []
    global sequenceCombinationDependMatrix
    sequenceCombinationDependMatrix = []
    for i in range(len(generalD)):
        lastElement.append(len(generalD[i]))
    print lastElement
    for i in range(Main.countComp):
        sequenceCombinationDependMatrix.append(1)


def ReNullGlovalVariables():
    global generalD
    generalD = []
    global arrayOfPossibleDLines
    arrayOfPossibleDLines = []
resultMatrix = []
def mainFunc ():

    realDependecyMatrix = []
    Main.read("ResultMatrix6.txt", resultMatrix)
    Main.read("DependMatrix6.txt",realDependecyMatrix)
    listPermutation = [k for k in range(len(resultMatrix))]
    allPermutations = list(itertools.permutations(listPermutation))

    for i in range(len (allPermutations)):

        ReNullGlovalVariables()
        global  resultMatrix
        resultMatrix = []
        for k in range(len(listPermutation[i])):
            resultMatrix.append(listPermutation[i][k])
            print resultMatrix
        findDependMatrix(resultMatrix[0],resultMatrix[1])
        setFisrtAndLastElementSequens()
        if [] in generalD:
            continue
        testDependMatrix()



def testDependMatrix():
    global sequenceCombinationDependMatrix
    for j in range(Main.countComp):
         sequenceCombinationDependMatrix[j] = 1
    while (getNextVarietyOfDependecyMatrix()):
        depMatr = []
        tmpMatr = []
        for k in range(len(sequenceCombinationDependMatrix)):
            tmpMatr.append(generalD[k][sequenceCombinationDependMatrix[k]-1])
        for k in range(len(tmpMatr)):
            tmparr = []
            for k1 in range(len(tmpMatr)):
                tmparr.append(-1)
            depMatr.append(tmparr)
        for k in range(len(tmpMatr)):
            for k1 in range(len(tmpMatr)):
                depMatr[k1][k] = tmpMatr[k][k1]
        #Now we have depend matrix and we should test is it works
        isCorrect = 1
        for i in range (1,len(resultMatrix)):
            testState = []
            Main.modelingNextState(resultMatrix[i],testState,depMatr,Main.countComp,Main.KState)
            val  = i + 1
            if val == len(resultMatrix):
                val = 0
            if testState != resultMatrix[val]:
                isCorrect = 0
                break
        if isCorrect == 1:
            print "Yes"
            print depMatr


#==================MAIN=CODE==================
lastElement = []
sequenceCombinationDependMatrix = []

mainFunc()

