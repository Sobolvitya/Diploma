from scipy.stats.stats import pearsonr
import Main
countStates = 101 #count of states in file (count state in cycle)
fileNameResult = ""
fileNameDepend = ""
def CalculatePirsonCorelation(size):#check order of matrix

    for i in range(size):
        aTemp = []
        for j in range(size):
            global matrixA
            cor = pearsonr(matrixA[i],matrixA[j])
            aTemp.append(cor[0])
        global pirsonMatrix
        pirsonMatrix.append(aTemp)


def setFileName(fileRes,fileDep):
    global fileNameResult,fileNameDepend
    fileNameResult = fileRes
    fileNameDepend = fileDep

def createDataSet( indexI, indexJ,numExpr):
    for i in range (1,countStates):
        global matrixA,pirsonMatrix,fileNameResult,fileNameDepend
        pirsonMatrix = []
        matrixA = []
        fileRes = fileNameResult + str(i)+".txt"
        Main.read(fileRes, matrixA)
        tmpDepMatrix = []
        fileDep = fileNameDepend + str(i)+".txt"
        Main.read(fileDep,tmpDepMatrix)
        global  size
        size = len(matrixA)
        CalculatePirsonCorelation(size)
        if i != numExpr :
            Main.write("Answer" + str(i)+".txt",[[tmpDepMatrix[indexI][indexJ]]])
            Main.write("DataMatrix"+ str(i)+".txt",pirsonMatrix)


def createTestDataSet(fileName, numExpr):
        global matrixA,pirsonMatrix,fileNameResult,fileNameDepend
        pirsonMatrix = []
        matrixA = []
        fileRes = fileNameResult + str(numExpr)+".txt"
        Main.read(fileRes, matrixA)
        global  size
        size = len(matrixA)
        CalculatePirsonCorelation(size)
        Main.write("DataMatrixExpr"+ str(numExpr)+".txt",pirsonMatrix)

#=========MAINCODE===========
#setFileName();
#setFileName("Result\\4x4\ResultMatrix","Result\\4x4\DependMatrix")
pirsonMatrix = []
matrixA = []
size = 0
#createDataSet(1,0)
