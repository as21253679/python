#https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/466616/
from sklearn.datasets import load_iris 
#載入資料集
iris = load_iris()
print("iris.data:-------\r\n",iris.data)          #輸出資料集
print("iris.target:-------\r\n",iris.target)        #輸出真實標籤
print("len(iris.target):-------\r\n",len(iris.target))
print("iris.data.shape:-------\r\n",iris.data.shape)    #150個樣本 每個樣本4個特徵
#匯入決策樹DTC包
from sklearn.tree import DecisionTreeClassifier
#訓練
clf = DecisionTreeClassifier()
clf.fit(iris.data, iris.target)
print("clf:-------\r\n",clf)
#預測
predicted = clf.predict(iris.data)
#獲取花卉兩列資料集
X = iris.data
L1 = [x[0] for x in X]
print("L1:-------\r\n",L1)
L2 = [x[1] for x in X]
print("L2:-------\r\n",L2)
#繪圖
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(L1, L2, c=predicted, marker='x')  #cmap=plt.cm.Paired
plt.title("DTC")
plt.show()