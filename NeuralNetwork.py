

from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import RPropMinusTrainer
from pybrain.supervised.trainers import BackpropTrainer
def readData(fileName):
    A = []
    file = open(fileName, 'r')
    for line in file:
        arr = line.split(' ')
        arr.remove('\n')
        try:
            arrTemp = [float(x) for x in arr]
            for i in arrTemp:
                A.append(i)
        except ValueError:
            print "err"
    file.close()

    return A


def readAnswer(fileName):
    file = open (fileName,'r')
    answer = 4
    for line in file:
        answer = int(line)
    return answer



def teachNeuralNetwork(countState,testNumber):

    data = tuple(readData("DataMatrix" + str(1) + ".txt"))
    size  = len(data)
    ds = ClassificationDataSet(size, 1,nb_classes=3,class_labels = ['0','1','-1'])

    #SET TRAINI DATA
    for i in range (1,countState):
        try:
            data = []
            data = (readData("DataMatrix" + str(i) + ".txt"))
            answer = readAnswer("Answer" + str(i) + ".txt")
            idx = 2 if answer == -1 else answer
            ds.appendLinked (data,[idx])
        except BaseException:
            l=1 #Just some fo catch it's not usefull


    ds._convertToOneOfMany()
    net = buildNetwork(ds.indim, 300, ds.outdim ,recurrent = True)
  #  trainer = RPropMinusTrainer(net, dataset = ds, momentum = 0.1, verbose = False,weightdecay=0.03)
    trainer = BackpropTrainer(net, dataset = ds, momentum = 0.1, verbose = False,weightdecay=0.03)
    trainer.trainUntilConvergence(maxEpochs= 2000)
    tstData =  (readData("DataMatrixExpr" + str(testNumber) + ".txt"))

    ansArr =  (net.activate(tstData))
    indx = 0
    max = ansArr[0]
    for i in range(len(ansArr)):
        if ansArr[i] > max:
            max = ansArr[i]
            indx = i
    t = [0,1,-1]

    return t[indx]



#========MAINCODE=============
#teachNeuralNetwork()