import pybrain
from pybrain.datasets import SupervisedDataSet
from pybrain.datasets import UnsupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer
import sys

from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer
from pybrain.supervised.trainers import RPropMinusTrainer

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



def teachNeuralNetwork():
    data = tuple(readData("DataMatrix" + str(1) + ".txt"))

    size  = len(data)
    ds = ClassificationDataSet(size, 1,nb_classes=3,class_labels = ['0','1','-1'])

    #SET TRAINI DATA
    for i in range (1,18):
        data = []
        if i == 5 or i == 6 or i == 7 or i == 8:
            continue
        data = (readData("DataMatrix" + str(i) + ".txt"))
        answer = readAnswer("Answer" + str(i) + ".txt")
        idx = 2 if answer == -1 else answer
        ds.appendLinked (data,[idx])

    ds._convertToOneOfMany()
    net = buildNetwork(ds.indim, 200, ds.outdim ,recurrent = True)
    trainer = RPropMinusTrainer(net, dataset = ds, momentum = 0.1, verbose = True,weightdecay=0.01)
    trainer.trainUntilConvergence(maxEpochs= 2000)
    tstData =  (readData("DataMatrix" + str(8) + ".txt"))


  #  ans = trainer.testOnClassData(dataset = tstData)

    #ts = UnsupervisedDataSet(size,)
   # ts.addSample(tstData)
  #  print ts

    ansArr =  (net.activate(tstData))
    indx = 0
    max = ansArr[0]
    for i in range(len(ansArr)):
        if ansArr[i] > max:
            max = ansArr[i]
            indx = i
    t = [0,1,-1]
    #ans = trainer.testOnData(tstData)
    print t[indx]



#========MAINCODE=============
teachNeuralNetwork()