import tensorflow as tf
import numpy as np

#创建数据
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

#搭建模型
weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights*x_data + biases

#计算误差
loss = tf.reduce_mean(tf.square(y-y_data))

#传播误差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#训练
init = tf.global_variables_initializer()  #初始化之前定义的所有Variable

sess = tf.Session()
sess.run(init)

for step in range(201):
	sess.run(train)
	if step % 20 == 0:
		print(step.sess.run(weights), sess.run(biases))