import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 資料轉為數字格式
def data_filter(data_set):
    length = len(data_set)
    width = int(data_set.size/length)
    for i in range(0,length):
        for j in range(0,width):
            data_set[i][j]=ord(data_set[i][j])
    data_set=data_set.astype(float)# 轉為float格式
    return data_set
	
# 讀入訓練用CSV
df = pd.read_csv("hw6_part4_data.csv")
train_data = np.array(df.iloc[:,2:24])
train_data = data_filter(train_data)# 過濾資料
ans = np.array(df.loc[:,'class'])
print(train_data)

# 讀入測試用CSV
df = pd.read_csv("hw6_part4_test.csv")
test_data = np.array(df.iloc[:,1:23])
test_data = data_filter(test_data)# 過濾資料

########################################################################
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

def PolynomialSVC(degree, C=1.0):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std)scaler', StandardScaler()),
        ('linearSVC', LinearSVC(C=C))
    ])

poly_svc = PolynomialSVC(degree=3)
poly_svc.fit(train_data, ans)

result = poly_svc.predict(test_data)
print(result)

########################################################################
from sklearn.svm import SVC

def PolynomialKernelSVC(degree, C=1.0):
    return Pipeline([
        ('std_scaler', StandardScaler()),
        ('kernelSVC', SVC(kernel='poly', degree=degree, C=C))
    ])

poly_kernel_svc = PolynomialKernelSVC(degree=3)
poly_kernel_svc.fit(train_data, ans)
result = poly_kernel_svc.predict(test_data)
print(result)


df = pd.read_csv("hw6_part4_data.csv")
X = np.array(df.loc[:,'cap-shape'])
y = np.array(df.loc[:,'cap-surface'])
#train_data = data_filter(train_data)# 過濾資料

# 繪圖
plt.scatter(X, y, alpha=0.5, s=50)
#plt.plot(sample, str, c='r')
plt.title('Linear Regression')
plt.show()
