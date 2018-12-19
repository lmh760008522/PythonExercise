import tensorflow as tf
import numpy as n

#添加一个神经层函数
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return output

#导入数据
x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

#利用占位符tf.placeholder()定义我们所需的神经网络的输入
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

#构建网络
#输入层1个、隐藏层10个、输出层1个的神经网络

#定义隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu) #tf.nn.relu是自带的激励函数
#定义输出层
prediction = add_layer(l1, 10, 1, activation_function=None)
#计算prediction和真实值的均方差
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))

train_step = tf.train.GradientDencentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)#在tensorflow中，只有session.run()才会执行我们定义的运算。

#训练
for i in range(1000):
	sess.run(train_step, feed_dict={xs:x_data,ys:y_data})
	#每隔50次训练刷新一次图形，用红色、宽度为5的线来显示我们的预测数据和输入之间的关系，并暂停0.1s
	if i%50 == 0:
		try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)

