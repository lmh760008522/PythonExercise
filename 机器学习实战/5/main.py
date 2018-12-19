import logRegres
from numpy import * 

dataArr, labelMat = logRegres.loadDataSet()
print(logRegres.gradAscent(dataArr, labelMat)) #打印回归系数

#打印随机梯度上升法拟合的回归系数
print(logRegres.stocGradAscent0(array(dataArr), labelMat))

#打印改进的随机梯度上升法拟合的回归系数
print(logRegres.stocGradAscent1(array(dataArr), labelMat))