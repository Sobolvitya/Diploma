
import PrepareDataForNN
import NeuralNetwork
import  Main
import time

def writeResultMatrix(matr,fileName):
    file = open(fileName, 'w')
    index = 0
    file.write("Size of matr   " + str(len(matr)) + "   \n")
    for m in matr:
        file.write("===== "+str(arrTestData[index]) + " =====\n")
        index += 1
        for Ai in m:
            for ak in Ai:
                file.write(str(ak) + " ")
            file.write("\n")
        file.write("========================\n")


def diffMatr(matr1,matr2):
    count1 = 0
    count2 = 0
    for i in range(len(matr1)):
        for j in range (len(matr2)):
            if matr1[i][j] != matr2[i][j]:
                count1 += 1
            if matr1[i][j] != matr2[j][i]:
                count2 += 1
    return count1,count2

#===========MAIN CODE===============
#test for 4x4 matrix
arrTestData = [12]#12,34,47,59,75]#2,3,6,10,34,56,78,82,94]
arrResultMatrix = []
t1 = time.time()
dimenssionMatrix = 4
for testDataNumber in arrTestData:
    arrResult = []
    middRes1 = []
    middRes2 = []
    print ("================TEST DATA NUMBER  - "  + str(testDataNumber) + " ==================")
    for i in range(dimenssionMatrix):
        arrTmp = []
        for j in range(dimenssionMatrix):
            print ("================PREPARE DATASET for[" + str(i) + "][" + str(j)+"]==============")
            PrepareDataForNN.setFileName("Result\\"+str(dimenssionMatrix)+"x"+str(dimenssionMatrix)+"\ResultMatrix","Result\\"+str(dimenssionMatrix)+"x"+str(dimenssionMatrix)+"\DependMatrix")
            PrepareDataForNN.createDataSet(i,j,testDataNumber)
            PrepareDataForNN.createTestDataSet("Result\\4x4\\test\ResultMatrix",testDataNumber)
            print ("================RUN NEURALNETWORK for[" + str(i) + "][" + str(j)+"]==============")
            tempRes = NeuralNetwork.teachNeuralNetwork(PrepareDataForNN.countStates,testDataNumber)
            arrTmp.append(tempRes)
        arrResult.append(arrTmp)
    tmpDepMatrix = []
    fileDep = "Result\\"+str(dimenssionMatrix)+"x"+str(dimenssionMatrix)+"\DependMatrix" + str(testDataNumber)+".txt"
    Main.read(fileDep, tmpDepMatrix)
    diff1, diff2 = diffMatr(arrResult, tmpDepMatrix)
    middRes1.append(diff1)
    middRes2.append(diff2)
    arrResultMatrix.append(arrResult)


writeResultMatrix(arrResultMatrix, "ResultMatrix.txt")
sum1 = 0
sum2 = 0
for i in range(len(middRes1)):
    print (str(middRes1[i]) + " : " + str(middRes2[i]))
    sum1 += middRes1[i]
    sum2 += middRes2[i]
res1 = float(sum1)/float(len(middRes1))
res2 = float(sum2)/float(len(middRes2))

print "============RESULT======================\n"
print ("============TOTAL TIME = " + str(time.time() - t1)+" ======")
print (str(res1) + "   :    " + str(res2))
file  =  open("ResultData.txt", 'w')
file.write("============RESULT======================\n")
file.write ("============TOTAL TIME = " + str(time.time() - t1)+" ======")
file.write (str(res1) + "   :    " + str(res2))
res1 = float((sum((int(middRes1[i]) for i in range(0, int(len(middRes1)))))))/float(len(middRes1))
res2 = float((sum((int(middRes2[i]) for i in range(0, int(len(middRes2)))))))/float(len(middRes2))
print (str(res1) + "   :    " + str(res2))
print "===========END=========================\n"

file.write (str(res1) + "   :    " + str(res2))
file.write("===========END=========================\n")
