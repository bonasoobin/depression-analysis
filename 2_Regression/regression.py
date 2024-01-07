import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor # 다중공산성
from sklearn.preprocessing import RobustScaler # scikit-learn 패키지의 RobustScaler 클래스

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.columns =  ['city','neighborhood','citynum','year','patient','age','population','stress','employment','covid','budget','public facilities','depression']
final.info()

fianl_dummy = pd.get_dummies(final, columns=['city']) # 
fianl_dummy.info()


Robust_X_num = final[['age','population','stress','employment','covid','budget','public facilities','depression']]
robustScaler = RobustScaler() # RobustScaler 객체 생성

# fit_transform()을 사용해서 학습과 스케일링을 한 번에 적용합니다.
X_train_robust = robustScaler.fit_transform(Robust_X_num)
# robust 스케일링이 완료된 데이터를 데이터프레임 형태로 변환합니다.
train_robust = pd.DataFrame(X_train_robust, 
                            index=Robust_X_num.index, 
                            columns=Robust_X_num.columns)

default_index = final[['city','neighborhood','citynum','year']]
final = pd.concat([default_index,train_robust], axis=1)
final.to_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final(preprocessing).csv')

# 다중공산성 확인

X_train_vif = final[['age','population','stress','employment','covid','budget','public facilities']]
vif = pd.DataFrame()
vif['VIF_Factor'] = [variance_inflation_factor(X_train_vif.values, i) 
                     for i in range(X_train_vif.shape[1])]
vif['Feature'] = X_train_vif.columns
vif

'''
스케일링 전
   VIF_Factor            Feature
0  166.870691                age
1    6.414972         population
2   33.127379             stress
3  180.983571         employment
4    1.448585              covid
5   12.064498             budget
6    4.263547  public facilities

스케일링 후
   VIF_Factor            Feature
0    2.692549                age
1    3.079997         population
2    1.281579             stress
3    1.853885         employment
4    1.383968              covid
5    1.317326             budget
6    2.189880  public facilities
'''

X_train_vif = fianl_dummy[['age','population','stress','employment','covid','budget','public facilities',
                           'city_강원도','city_경기도','city_경상남도','city_경상북도','city_광주광역시',
                           'city_대구광역시','city_대전광역시','city_부산광역시','city_서울특별시','city_세종특별자치시',
                           'city_울산광역시','city_인천광역시','city_전라남도','city_전라북도','city_제주특별자치도',
                           'city_충청남도','city_충청북도']]
vif = pd.DataFrame()
vif['VIF_Factor'] = [variance_inflation_factor(X_train_vif.values, i) 
                     for i in range(X_train_vif.shape[1])]
vif['Feature'] = X_train_vif.columns
vif


'''
스케일링 전
    VIF_Factor            Feature
0     3.434501                age
1     4.559608         population
2     1.427780             stress
3     2.483534         employment
4     1.411427              covid
5     2.931897             budget
6     2.796617  public facilities
7    37.038297           city_강원도
8    79.722185           city_경기도
9    42.862526          city_경상남도
10   49.990887          city_경상북도
11   10.464532         city_광주광역시
12   15.163368         city_대구광역시
13   10.207353         city_대전광역시
14   28.604092         city_부산광역시
15   49.727016         city_서울특별시
16    2.805822       city_세종특별자치시
17    9.414152         city_울산광역시
18   21.198656         city_인천광역시
19   46.137015          city_전라남도
20   32.437579          city_전라북도
21    5.278927       city_제주특별자치도
22   34.244522          city_충청남도
23   28.587732          city_충청북도

스케일링 후 
    VIF_Factor            Feature
0     3.434501                age
1     4.559608         population
2     1.427780             stress
3     2.483534         employment
4     1.411427              covid
5     2.931897             budget
6     2.796617  public facilities
7     1.427298           city_강원도
8     1.310426           city_경기도
9     1.388465          city_경상남도
10    1.264269          city_경상북도
11    1.134227         city_광주광역시
12    1.157730         city_대구광역시
13    1.069699         city_대전광역시
14    1.233919         city_부산광역시
15    1.525840         city_서울특별시
16    1.043241       city_세종특별자치시
17    1.036529         city_울산광역시
18    1.186370         city_인천광역시
19    1.326379          city_전라남도
20    1.568944          city_전라북도
21    1.065625       city_제주특별자치도
22    1.376551          city_충청남도
23    1.158498          city_충청북도

'''
