import matplotlib.pyplot as plt

#squares = [1,4,9,16,25]
#plt.plot(squares)
#plt.show()

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
	edgecolor='none', s=40)
plt.show()
plt.savefig('squares_plot.png')