from numpy import *

'''
1.准备数据：从文本中构建词向量
把文本看成单词向量或者词条向量，也就是说将句子转换为向量。
'''
#加载数据集
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1] #1表示侮辱性文字，0表示正常言论（人工标注的结果，用于训练）
    return postingList,classVec

#创建一个包含在所有文档中出现的不重复词的列表
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #创建两个集合的并集
    return list(vocabSet)

#词表到向量的转换函数
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList) #创建一个其中所含元素都为0的向量
    for word in inputSet:
        if word in vocabList: #单词在输入文档中出现
            returnVec[vocabList.index(word)] = 1
        else: print ("the word: %s is not in my Vocabulary!" % word)
    return returnVec


'''
2.训练算法：从词向量计算概率
伪代码：
计算每个类别中的文档数目
对每篇训练文档：
    对每个类别：
    	如果词条出现在文档中 -> 增加该词条的计数值
    	增加所有词条的计数值
    对每个类别：
    	对每个词条：
    		将该词条中的数目除以总词条数目得到条件概率
    返回每个类别的条件概率
'''
def trainNB0(trainMatrix,trainCategory):#参数：文档矩阵，每篇文档类别标签所构成的向量
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    #计算文档属于侮辱性文档的概率p1
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    '''
    问题一：初始化概率
    利用贝叶斯分类器对文档进行分类时，要计算多个概率的乘积以获得文档属于某个类别的概率。
    如果其中一个概率值为0 ,那么最后的乘积也为0。
    为降低这种影响，可以将所有词的出现数初始化为1，并将分母初始化为2。
    '''
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    #遍历训练集中的所有文档
    for i in range(numTrainDocs):
    	#若出现侮辱性词汇
        if trainCategory[i] == 1:
        	#向量相加
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    '''
    问题二：下溢出
    当计算乘积时,由于大部分因子者3非常小，所以程序会下溢出或者得到不正确的答案。
    一种解决办法是对乘积取自然对数。 
    ln(a*b) = ln(a) + ln(b)
    于是通过求对数可以避免下溢出或者浮点数舍入导致的错误。
    同时，采用自然对数进行处理不会有任何损失。
    '''
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive


'''
3.测试算法
'''
#朴素贝叶斯分类函数
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1): #输入：要分类的向量，三个概率
    #两个向量对应元素相乘
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    #将词汇表中所有词的对应值相加，然后将该值加到类别的对数概率上。    
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    #比较类别的概率返回大概率对应的类别标签
    if p1 > p0:
        return 1
    else: 
        return 0

#遍历函数（封装所有操作，节省输入代码时间）
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))


'''
4.准备数据：文档词袋模型
词集模型：每个词的出现与否作为一个特征
词袋模型：如果每个词在文档中出现不止一次，这可能意味着包含该词是否出现在文档中所不能表达的某种信息。
'''
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1 #每出现一次都加1，而不是设置成1
    return returnVec