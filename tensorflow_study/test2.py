import tensorflow as tf

#创建两个矩阵
matrix = tf.constant([[3,3]])
matrix = tf.constant([[2],[2]])
product = tf.matmul(matrix1, matrix2) #输出矩阵相乘结果

#因为 product 不是直接计算的步骤
#所以我们会要使用 Session 来激活 product 并得到计算结果.

#方法1
sess = tf.Session()
result = sess.run(product)
print("method1:",result)
sess.close()

#方法2
with tf.Session() as sess:
	result2 = sess.run(product)
	print("method2:",result2)