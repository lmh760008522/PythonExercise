#导入模块
from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression #这次我们使用线性回归
import matplotlib.pyplot as plt

#导入数据-训练模型
loaded_data = datasets.load_boston()  #加载数据
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()  #定义模型
model.fit(data_X,data_y) #训练模型

print(model.predict(data_X[:4, :])) #打印预测值
print(data_y[:4])  #打印真实值
