import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final.columns = ['city','neighborhood','citynum','year','patient','age','population',
                 'stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

# train_test_split 사용하여 모델링

X_train, X_test , y_train , y_test = train_test_split(X,y, test_size = 0.3, random_state=42)

robust_scaler = RobustScaler()
X_train_robust = robust_scaler.fit_transform(X_train)
X_test_robust = robust_scaler.fit_transform(X_test)

def poly_regression(deg) :
    deg = deg
    poly = PolynomialFeatures(degree=deg)
    # deg차 다항식으로 변환한 결과를 반환, 
    # 결과는 NumPy 배열 형태이며, 각 행은 샘플 각 열은 다항식 항을 나타냄
    # 각 독립 변수마다 1차 및 2차 항이 생성되고, 이들을 모두 합치면 총 165개의 다항식 항이 생성 ---------> ??????
    X_train_poly = poly.fit_transform(X_train_robust) # 훈련 데이터에 대해 PolynomialFeatures 적용
    X_test_poly = poly.transform(X_test_robust) # 테스트 데이터에 대해 훈련 데이터에서 학습한 변환을 적용

    # 다항 회귀 모델 훈련
    model = LinearRegression() 
    model.fit(X_train_poly, y_train) # Numpy 배열형태인 X_train_poly를 다항 회귀식으로 모델링

    # 훈련된 모델로 예측
    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    # 모델 평가 (RSME)
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

    # 모델 평가 (R^2)
    train_R = r2_score(y_train, y_train_pred)
    test_R = r2_score(y_test, y_test_pred)
    
    # 회귀식의 계수(coefficients)와 절편(intercept) 확인
    coefficients = model.coef_  
    intercept = model.intercept_
    
    #print(f'계수 : {coefficients}')
    #print(f'절편 : {intercept}')
    print(f'RMSE(train): {train_rmse}')
    print(f'RMSE(test): {test_rmse}')
    print(f'R^2(train) : {train_R}')
    print(f'R^2(test) : {test_R}')

    return

poly_regression(2)
'''
RMSE(train): 0.3696770631879331
RMSE(test): 0.7929366615188352
R^2(train) : 0.9141985517115875
R^2(test) : 0.47630130027766704
'''
poly_regression(3)
'''
RMSE(train): 0.1774223265946573
RMSE(test): 9.052804058033015
R^2(train) : 0.9802363957995633
R^2(test) : -67.26070047179567
'''
poly_regression(4)
'''
RMSE(train): 0.05760498952741049
RMSE(test): 607.6981355401302
R^2(train) : 0.997916613662222
R^2(test) : -307594.7336206796
'''

# 결론 : 과적합이 일어난 것 같다.