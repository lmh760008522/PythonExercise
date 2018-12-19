from numpy import *

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('E:/电子书/机器学习实战代码/机器学习实战代码/Ch05/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split() #每行前2个值为两个特征x1,x2，第三个值是数据对应的类别标签
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) #x0 = 1,两个特征x1,x2
        labelMat.append(int(lineArr[2])) #数据对应的类别标签
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

#梯度上升
#参数一：一个2维numpy数组，列分别代表每个不同的特征，每行则代表每个训练样本。
#参数二：类别标签。（这里是一个行向量，需要做转置）
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #转化为NumPy矩阵 
    labelMat = mat(classLabels).transpose() #转化为NumPy矩阵 
    m,n = shape(dataMatrix)
    alpha = 0.001 #步长
    maxCycles = 500 #迭代次数
    weights = ones((n,1))
    for k in range(maxCycles):              #重矩阵运算
        h = sigmoid(dataMatrix*weights)     #矩阵相乘，得到一个列向量
        error = (labelMat - h)              #矢量相减
        weights = weights + alpha * dataMatrix.transpose()* error
    return weights

#伪随机梯度上升
def stocGradAscent0(dataMatrix, classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)   #initialize to all ones
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

#改进的随机梯度上升
def stocGradAscent1(dataMatrix, classLabels, numIter=150): #改进3
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = list(range(m))  #原书为： dataIndex = range(m)
        for i in range(m):
        	#改进一
            alpha = 4/(1.0+j+i)+0.0001    #alpha每次迭代时调整
            #改进二
            randIndex = int(random.uniform(0,len(dataIndex)))#随机选取更新
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights