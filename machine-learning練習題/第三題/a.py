from sklearn.tree import DecisionTreeClassifier #匯入決策樹DTC包
import numpy as np
import pandas as pd

array = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'] # 設定預測因子
# 讀入訓練用CSV
df = pd.read_csv("hw6_part3_data.csv")
df=df.fillna(value=0)# 空格補0
train_data = np.array(df.loc[:,array])
ans = np.array(df.loc[:,'target'])

#訓練
clf = DecisionTreeClassifier()
clf.fit(train_data, ans)

# 讀入測試用CSV
df = pd.read_csv("hw6_part3_test.csv")
df=df.fillna(value=0)# 空格補0
test_data = np.array(df.loc[:,array])

#預測
predicted = clf.predict(test_data)
print(predicted)