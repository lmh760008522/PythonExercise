#导入模块
from sklearn import datasets #用自带数据库ins
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#创建数据
iris = datasets.load_iris()
iris_x = iris.data  #属性存在x
iris_y = iris.target  #类别标签存y

#此时打印x和y可发现，属性有4中，类别有3类

#把数据集分为训练集和测试集
#test_size=0.3 ==> 测试集占总数据的 30%
x_train,x_test,y_train,y_test=train_test_split(iris_x,iris_y,test_size=0.3)

#此时打印x_train,x_test,y_train,y_test，可以看到分开后的数据集顺序也被打乱
#这样更有利于学习模型

#建立模型－训练－预测
knn = KNeighborsClassifier() #定义模块方式
knn.fit(x_train,y_train) #用 fit 来训练 training data
#此时knn已经变成了训练好的模型
print(knn.predict(x_test)) #打印预测值
print(y_test) #打印真实值（用于对比）