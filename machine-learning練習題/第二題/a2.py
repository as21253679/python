import numpy as np
import matplotlib.pyplot as plt  # 导入绘图库
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
            if data_set[i][j]=='S':
                data_set[i][j]=1
            elif data_set[i][j]=='C':
                data_set[i][j]=2
            elif data_set[i][j]=='Q':
                data_set[i][j]=3
            if is_number(data_set[i][j])==False:
                data_set[i][j]=0
    data_set=data_set.astype(float)# 轉為float格式
    return data_set
	
# 不告訴你這函式是幹嘛的
def asd(data_set1,data_set2):
    TP=0;FP=0;
    FN=0;TN=0;
	
    length = len(data_set1)
    for i in range(0,length):
        if data_set1[i]==1 and data_set2[i]==1:
            TP=TP+1
        elif data_set1[i]==1 and data_set2[i]==0:
            FP=FP+1
        elif data_set1[i]==0 and data_set2[i]==1:
            FN=FN+1
        elif data_set1[i]==0 and data_set2[i]==0:
            TN=TN+1
    return TP,FP,FN,TN
	
array=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked'] # 設定預測因子
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
df = pd.read_csv("hw6_part2_data.csv")
df=df.fillna(value=0)# 空格補0
test_data = np.array(df.loc[:,array])
test_data = data_filter(test_data)# 過濾資料

# 預測結果
result=regr.predict(test_data)
print(result)

# ROC
TP,FP,FN,TN=asd(result,ans)
print(TP,FP)
print(FN,TN)
Sensitivity = TP/(TP+FN)
Specificity = TN/(FP+TN)

# 繪圖
plt.scatter(1-Specificity, Sensitivity, alpha=0.5, s=50)
plt.plot([0,1],[0,1],c='r')
plt.title('ROC Curve')
plt.show()


from sklearn.metrics import roc_curve, auc  ###计算roc和auc
def acu_curve(y,prob):
    fpr,tpr,threshold = roc_curve(y,prob) ###计算真正率和假正率
    roc_auc = auc(fpr,tpr) ###计算auc的值
 
    plt.figure()
    lw = 2
    plt.figure(figsize=(10,10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc) ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
 
    plt.show()
	
acu_curve(ans,result)
