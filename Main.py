
import random
#from pybrain.tools.shortcuts import buildNetwork
FILENAME = "ExprResult.txt"
KState = 5
countComp = 4
influenceCoef =0.5
thereholds = 2
startCycle = 0
endCycle =0

arrStartPoints = []


def write(fileName,A):
    file = open(fileName, 'w')
    for Ai in A:
        for ak in Ai:
            file.write(str(ak) + " ")
        file.write("\n")
    file.close()



def parseString(str):
    arr = []
    tmp = ""
    for i in range(len(str)):
        if(str[i] == ' '):
            arr.append(int(tmp))
            tmp = ""
        else:
            tmp += str[i]
    return arr


def read(fileName,A):
    file = open(fileName, 'r')
    for line in file:
        arr = parseString(line)
        A.append(arr)
    file.close()



def getExprData():
    return random.randint(1,KState)


def setMatrix(A, sizeK, sizeT):
    #A = []
    for k in range(sizeK):
        Ai = []
        for t in range(sizeT):
            ak = getExprData()
            Ai.append(ak)
        A.append(Ai)






#====================MODELING DATA CODE====================

def getDependecyPair():
     i = random.randint(-1,1)
     j = random.randint(-1,1)
     return (i,j)

def  createDependencyMatrix (A, sizeN):
    for i in range(sizeN):
        Ai = []
        for j in range (sizeN):
            k = random.randint(-1,1)

            #ak = getDependecyPair()
            #if(i == j ):
             #   Ai.append(0)
            #else:
               # k = (random.randint(0,1))
                #if k == 0: k = -1
            Ai.append(k)

        A.append(Ai)


def createStateComponentWithNormalVarite(A,sizeN,maxK):
    for i in range (sizeN):
        tmp = random.randint(1,maxK);
        #tmp = int(random.normalvariate(maxK/2,maxK/4))
        tmp = tmp if (tmp < KState) else KState
        tmp = tmp if tmp >= 1 else 1
        A.append(tmp)

def modelingNextState(prevState,nextState,dependMatrx,sizeN,maxValue):
    for i in range(sizeN):
        tmp = prevState[i]
        di =0;
        for j in range(sizeN):
            koef = 0;
            koef = dependMatrx[j][i]
            if prevState[j] != 0:
                di += koef * prevState[j]
        if di > thereholds:
            tmp += 1
        if di < - thereholds:
            tmp -= 1
        tmp = tmp if (tmp < maxValue) else maxValue
        tmp = tmp if tmp >= 1 else 1
        nextState.append(tmp)


def modelingWholeLoop(stMatr,dpMatr,tstMatr,countIteration, testFlag):
    tstMatr.append(stMatr)
    nxtMatr = []
    print "Start"
    flag = 0
    for i in range(countIteration):
        modelingNextState(stMatr,nxtMatr,dpMatr,countComp,KState)
        tstMatr.append(nxtMatr)

        #CHEK if len(cycle == 0)
        if tstMatr[i+1] == tstMatr[i]:
            break
        #CHECK aLL possible cycle before i
        for j in range(len(tstMatr)-1):
            if(tstMatr[j] == tstMatr[i+1]):
                startCycle = j
                endCycle = i+1
                flag  = 1
                break;

        if flag == 1:
            break;
        stMatr = nxtMatr
        nxtMatr = []

    print "Finish"
    if flag == 1:
        flagUsing = 1
        for i in range(len(arrStartPoints)):
            if tstMatr[startCycle] == arrStartPoints [i]:
                flagUsing = 0
                testFlag.append(0)
                break
        if flagUsing == 1:
            testFlag.append(1)
            tmpMatr = []
            for i in range(startCycle,endCycle,1):
                tmpMatr.append(tstMatr[i])
            tstMatr = []
            global countCycle
            fileN1 = "Result\ResultMatrix" + str(countCycle) + ".txt"
            write(fileN1,tmpMatr)
            fileN2 = "Result\DependMatrix" + str(countCycle) + ".txt"
            write(fileN2,dpMatr)
            arrStartPoints.append(tmpMatr[0])

    else:
        testFlag.append(0)
        write ("Result\NotResultMatrix.txt",tstMatr)


def loopModeling():

    for i in range(1000000):
        stMatr = []
        dpMatr = []
        nxtMatr = []
        createStateComponentWithNormalVarite(stMatr,countComp,KState)
       # stMatr = [1,4,3]
        createDependencyMatrix(dpMatr, countComp)
       # write("DependMatrix.txt",dpMatr)
        #read("DependMatrix.txt",dpMatr)
        print "depMatr"
        print dpMatr
        print "stMatr"
        print stMatr



        tstMatr = []
        testFlag = []
        modelingWholeLoop(stMatr,dpMatr,tstMatr,1000,testFlag)
        global countCycle
        if testFlag[0] == 1:
            countCycle = int(countCycle) + 1



#=================================MAIN CODE==============================================
countCycle = 1;
#loopModeling()

#setMatrix(A, 4, 5)
#write(A)
#read(A)

