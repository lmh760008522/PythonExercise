
#用函数来建立 100 个 sample，有一个 feature，和一个 target，这样比较方便可视化。
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)

#用 scatter 的形式来输出结果
plt.scatter(X, y)
plt.show()