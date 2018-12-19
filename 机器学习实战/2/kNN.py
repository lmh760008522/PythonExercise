from numpy import *
import operator
from os import listdir

#创建数据集和标签
def createDataSet():
	group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

#从文本文件中解析数据
'''
对未知类别属性的数据集中的每个点依次执行以下操作：
(1)计算已知类别数据集中的点与当前点之间的距离；
(2)按照距离递增次序排序；
(3)选取与当前点距离最小的走个点；
(4)确定前灸个点所在类别的出现频率；
(5)返回前女个点出现频率最高的类别作为当前点的预测分类。
'''
#使用k-近邻算法将每组数据划分到某个类中
def classify0(inX, dataSet, labels,k): #参数分别为：输入向量，输入训练样本集，标签向量， 最临近邻居的数目
	dataSetSize = dataSet.shape[0]
	#欧式距离计算
	diffMat = tile(inX, (dataSetSize,1)) - dataSetSize # tile(A，rep) 重复A的各个维度 
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	#根据距离排序
	sortedDistIndicies = distances.argsort()
	#选择距离最小的k个点
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	#排序
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]
