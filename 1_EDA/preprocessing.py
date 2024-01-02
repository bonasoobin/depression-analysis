import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

final_data = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final_data.isnull()
final_data['우울증지수'] = round((final_data['우울증환자수']/final_data['총인구수'])*100, 2) 
final_data.info()
final_data.columns = ['city','neighborhood','citynum','year','patient','age','population','stress','employment','covid','budget','public facilities','depression']

final_data[['patient','age','population','stress','employment','covid','budget','public facilities','depression']].describe()

'''
            patient          age     population       stress  employment          covid       budget  public facilities   depression
count   1250.000000  1250.000000    1250.000000  1250.000000  1250.00000    1250.000000   1250.00000        1250.000000  1250.000000        
mean    3776.165600    46.026720  206866.232000    25.172800    62.10044   23230.667200   6624.11040          75.183200     1.655536        
std     4074.322496     4.944874  166228.852267     4.360287     5.61868   62572.915299   2275.40401          74.886116     2.180987        
min        0.000000    36.000000    8867.000000     6.200000    46.35000       0.000000   2758.00000           0.000000     0.000000        
25%      515.250000    42.200000   55743.000000    22.500000    58.36250       0.000000   5298.00000          23.000000     0.682500        
50%     2889.000000    44.800000  176398.500000    25.500000    60.70000      84.000000   6207.00000          56.000000     1.390000        
75%     5581.250000    50.100000  312786.500000    28.100000    65.73750    3100.250000   8050.00000         108.000000     2.127500        
max    32947.000000    58.800000  910814.000000    39.800000    84.60000  564132.000000  13975.00000         617.000000    34.800000        

'''

# 이상치와 산점도 확인

def cheak_eda(name) :
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=final_data[f"{name}"], y=final_data['depression'], color='blue')
    plt.title('Scatter Plot of Depression Score vs. Age')
    plt.xlabel('Age')
    plt.ylabel('Depression Score')
    plt.savefig(f"{name}과 depression의 산점도.png")
    plt.close()

    plt.figure(figsize=(10,20))
    box = final_data.boxplot(column=[f"{name}"])
    plt.savefig(f"{name}의 boxplot.png")
    plt.close()

index_name = ['age','population','stress','employment','covid','budget','public facilities','depression']
for i in index_name :
    cheak_eda(i)

final_data[final_data['budget'] == 13975] # 전라북도 -> 확인완 (오류아님)

'''
age 제외 이상치 모두 존재 
이상치가 있을 때 RobustScaler 사용
'''

import pingouin as pg 
pg.normality(final_data['population'])



'''
from sklearn.preprocessing import RobustScaler # scikit-learn 패키지의 RobustScaler 클래스

Robust_X_num = final_data[['age','population','stress','employment','covid','budget','public facilities','depression']]
robustScaler = RobustScaler() # RobustScaler 객체 생성

# fit_transform()을 사용해서 학습과 스케일링을 한 번에 적용합니다.
X_train_robust = robustScaler.fit_transform(Robust_X_num)
# robust 스케일링이 완료된 데이터를 데이터프레임 형태로 변환합니다.
train_robust = pd.DataFrame(X_train_robust, 
                            index=Robust_X_num.index, 
                            columns=Robust_X_num.columns)

default_index = final_data[['city','neighborhood','citynum','year']]
final = pd.concat([default_index,train_robust], axis=1)

final.to_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final(preprocessing).csv')

'''