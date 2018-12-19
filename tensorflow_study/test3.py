import tensorflow as tf

#定义两个输入
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

#做乘法运算，并输出为output
output = tf.multiply(input1, input2)

with tf.Session() as sess:
	print(sess.run(output, feed_dict={input1:[7.], input2:[2.]}))