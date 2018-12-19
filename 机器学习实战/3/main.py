import trees
myDat, labels = trees.createDataSet()

#测试calcShannonEnt()函数
print(trees.calcShannonEnt(myDat))
'''
熵越高，则混合的数据也越多
在数据集中添加更多的分类，观察熵是如何变化的。
'''
myDat[0][-1] = 'maybe'
print(trees.calcShannonEnt(myDat))

#测试splitDataSet()函数
print(trees.splitDataSet(myDat,0,1))
print(trees.splitDataSet(myDat,0,0))

#测试chooseBestFeatureToSplit()函数
print(trees.chooseBestFeatureToSplit(myDat))
print(myDat)

#测试createTree()函数
myTree = trees.createTree(myDat,labels)
print(myTree)

#测试classify()函数
trees.classify(myTree,labels,[1,0])
trees.classify(myTree,labels,[1,1])

trees.storeTree(myTree,'classifierStorage.txt')
trees.grabTree('classifierStorage.txt')