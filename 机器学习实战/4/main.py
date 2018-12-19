import bayes
from numpy import *

listOPosts, listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts) #创建一个包含所有词的列表
print(myVocabList)

print(bayes.setOfWords2Vec(myVocabList, listOPosts[0]))

trainMat = []
for postinDoc in listOPosts:
	trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))

p0v, p1v, pAb = bayes.trainNB0(trainMat, listClasses)

#输出任意文档属于侮辱性文档的概率
print(pAb)

bayes.testingNB()


