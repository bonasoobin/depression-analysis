# 로그, 지수, 제곱 변환하여도 선형 관계가 되지 않음 -> 사용 XXXXXXX

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final.columns = ['city','neighborhood','citynum','year','patient','age','population',
                 'stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

X_log = np.log(X)
X_log_df = pd.DataFrame(X_log,columns = X.columns)

X_log_df.corr()

def cheak_eda(name) :
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=X_log_df[f"{name}"], y=y, color='blue')
    plt.title(f"Scatter Plot of Depression Score vs{name}")
    plt.xlabel(f"{name}")
    plt.ylabel('Depression Score')
    plt.savefig(f"{name}과 depression의 산점도.png")
    plt.close()

for i in ['patient','age','population','stress','employment','covid','budget', 'public facilities']  :
    cheak_eda(i)