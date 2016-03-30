import Main


def findDependMatrix (A1, A2):
    arrDepemMatrix = []
    for i in range(len(A1)):
        diff = A2[i] - A1[i]
        if diff == 1:
            #Тут должна быть функция перебора, вынести в отдельную функцию
            return 1;
        if diff == 0:
            return 0;
        if diff == -1:
            return -1

def mainLoop(resultMatrix):
    A1 = resultMatrix[0]

    for i in range(1,len(resultMatrix)):



def mainFunc ():
    resultMatrix = []
    realDependecyMatrix = []

    Main.read("ResultMatrix6.txt", resultMatrix)
    Main.read("DependMatrix6.txt",realDependecyMatrix)

#==================MAIN=CODE==================

mainFunc()
