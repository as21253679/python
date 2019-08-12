import numpy as np
from sklearn import linear_model
import pandas as pd

# 字串非float判斷
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass 
    return False

# 過濾資料函式
def data_filter(data_set):
    length = len(data_set)
    width = int(data_set.size/length)
    for i in range(0,length):
        for j in range(0,width):
            if is_number(data_set[i][j])==False:
                data_set[i][j]=0
    data_set=data_set.astype(float)# 轉為float格式
    return data_set
	
# 不告訴你這函式是幹嘛的
def asd(data_set1,data_set2):
    a=0
    b=0
    length = len(data_set1)
    for i in range(0,length):
        if data_set1[i]==data_set2[i]:
            a=a+1
        else:
            b=b+1
    print(a,b)
	
array=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked'] # 設定預測因子
#array=['Sex'] # 設定預測因子
# 讀入訓練用CSV
df = pd.read_csv("hw6_part2_data.csv")
df=df.fillna(value=0)# 空格補0
train_data = np.array(df.loc[:,array])
ans = np.array(df.loc[:,'Survived'])
train_data = data_filter(train_data)# 過濾資料

# 建立及訓練模型
regr = linear_model.LogisticRegression()
regr.fit(train_data, ans)
#print(regr.coef_)# 訓練後的模型

# 讀入測試用CSV
df = pd.read_csv("hw6_part2_test.csv")
df=df.fillna(value=0)# 空格補0
test_data = np.array(df.loc[:,array])
test_data = data_filter(test_data)# 過濾資料

# 預測結果
result=regr.predict(test_data)
print(result)

#asd(result,ans)
