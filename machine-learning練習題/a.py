#import numpy as np
import matplotlib.pyplot as plt  # 导入绘图库
from sklearn import linear_model

# 宣告資料
X = [[1],[2],[3],[4],[5],[6]]
y = [2, 4, 6, 8, 10, 10]
sample=[[5],[1],[0],[10]]

# 建立及訓練模型
regr = linear_model.LinearRegression()
#regr = linear_model.LogisticRegression()
regr.fit(X, y)
print(regr.coef_)

# 預測
str=regr.predict(sample)
print(str)

# 繪圖
plt.scatter(X, y, alpha=0.5, s=50)
plt.plot(sample, str, c='r')
plt.title('Linear Regression')
plt.show()
