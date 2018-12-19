import tensorflow as tf

#四个参数：输入值、输入的大小、输出的大小和激励函数
#设定默认的激励函数是None
def add_layer(inputs, in_size, out_size, activation_function=None):
	#weights为一个in_size行, out_size列的随机变量矩阵
	weights = tf.Variable(tf.random_normal([in_size, out_size]))
	biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
	#定义Wx_plus_b, 即神经网络未激活的值
	Wx_plus_b = tf.matmul(inputs, weights) + biases

	if activation_function is None:
		outputs = Wx_plus_b
	else:
		outputs = activation_function(Wx_plus_b)
	return outputs
