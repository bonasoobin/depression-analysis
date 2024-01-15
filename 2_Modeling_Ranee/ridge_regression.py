import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import Ridge 
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final.columns = ['city','neighborhood','citynum','year','patient','age','population',
                 'stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

robust_scaler = RobustScaler()

# 릿지회귀로 규제주기 (모든 특성이 중요하거나 특성관 상관관계가 높은 경우)
def ridge_poly_regression(num) :
    X_train, X_test , y_train , y_test = train_test_split(X,y, test_size = 0.3, random_state=123)  
    X_train_robust = robust_scaler.fit_transform(X_train)
    X_test_robust = robust_scaler.fit_transform(X_test)
    
    poly = PolynomialFeatures(degree=num)
    X_train_poly = poly.fit_transform(X_train_robust) 
    X_test_poly = poly.transform(X_test_robust) 

    for a in [0,0.1,1] :
       
        # 릿지 회귀 모델
        model = Ridge(alpha=a)
        model.fit(X_train_poly, y_train) 

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
        print(f'규제가 {a}일 때 RMSE(train): {train_rmse}')
        print(f'규제가 {a}일 때 RMSE(test): {test_rmse}')
        print(f'규제가 {a}일 때 R^2(train) : {train_R}')
        print(f'규제가 {a}일 때 R^2(test) : {test_R}')
        print()

    return
ridge_poly_regression(2)
'''
규제가 0일 때 RMSE(train): 0.3696775641061013
규제가 0일 때 RMSE(test): 0.7953663572915005
규제가 0일 때 R^2(train) : 0.914198319186837
규제가 0일 때 R^2(test) : 0.47308697547772627

규제가 0.1일 때 RMSE(train): 0.3697281163736232
규제가 0.1일 때 RMSE(test): 0.7982605777027281
규제가 0.1일 때 R^2(train) : 0.9141748513515597
규제가 0.1일 때 R^2(test) : 0.46924528153245537

규제가 1일 때 RMSE(train): 0.37319117460349005
규제가 1일 때 RMSE(test): 0.8586728818040422
규제가 1일 때 R^2(train) : 0.9125595593688247
규제가 1일 때 R^2(test) : 0.3858704503545103
'''
# 결론 : 규제 전이나 후나 별 다른거 없는데...?


def ridge_cross_poly_regression(num) :
    poly = PolynomialFeatures(degree=num)
    X_robust = robust_scaler.fit_transform(X)
    X_poly = poly.fit_transform(X_robust)    
    
    for a in [0,0.1,1] :

        model = Ridge(alpha=a)

        # rmse
        cv_result_rmse = cross_val_score(model, X_poly, y, cv=10,
                                        scoring='neg_mean_squared_error')
        cv_rmse = np.sqrt(-cv_result_rmse) # 음수의 평균 제곱 오차를 양수로 변환
        avg_cv_rmse = np.mean(cv_rmse)
        std_cv_rmse = np.std(cv_rmse)

        # R^2
        cv_result_R = cross_val_score(model, X_poly, y, cv=10,
                                        scoring='r2')
        avg_cv_R = np.mean(cv_result_R)

        print(f'규제가 {a}일 때 교차검증 RMSE: {cv_rmse}')
        print(f'규제가 {a}일 때 교차검증 평균 RMSE: {avg_cv_rmse}')
        print(f'교차검증 표준편차 RMSE: {std_cv_rmse}')
        print(f'규제가 {a}일 때 교차검증 R^2: {cv_result_R}')
        print(f'규제가 {a}일 때 교차검증 평균 R^2: {avg_cv_R}')

        # 교차검증 예측값 생성
        y_pred_cv = cross_val_predict(model, X_poly, y, cv=10)

        # 교차검증 RMSE 및 R^2 계산
        cv_pred_rmse = np.sqrt(mean_squared_error(y, y_pred_cv))
        cv_pred_r2 = r2_score(y, y_pred_cv)

        print(f'교차검증 예측값 RMSE: {cv_pred_rmse}')
        print(f'교차검증 예측값 R^2: {cv_pred_r2}')

    return
ridge_cross_poly_regression(2)
'''
규제가 0일 때 교차검증 평균 RMSE: 0.45024755594344634
규제가 0일 때 교차검증 평균 R^2: 0.8132383348195557
규제가 0.1일 때 교차검증 평균 RMSE: 0.4495949176697528
규제가 0.1일 때 교차검증 평균 R^2: 0.8134599268789694
규제가 1일 때 교차검증 평균 RMSE: 0.44416286320900944
규제가 1일 때 교차검증 평균 R^2: 0.82089376469293
'''

# 릿지함수로 규제를 주고 교차검증을 할 때 예측력이 높은 모델링이 가능


def ridge_cross_poly_regression(num) :

    poly = PolynomialFeatures(degree=num)
    X_robust = robust_scaler.fit_transform(X)
    X_poly = poly.fit_transform(X_robust)    
    

    model = Ridge(alpha=1)
    model.fit(X_poly, y)
    coefficients = model.coef_  
    intercept = model.intercept_
    
    print(f'계수 : {coefficients}')
    print(f'절편 : {intercept}')

    # rmse
    cv_result_rmse = cross_val_score(model, X_poly, y, cv=10,
                                    scoring='neg_mean_squared_error')
    cv_rmse = np.sqrt(-cv_result_rmse) # 음수의 평균 제곱 오차를 양수로 변환
    avg_cv_rmse = np.mean(cv_rmse)
    std_cv_rmse = np.std(cv_rmse)

    # R^2
    cv_result_R = cross_val_score(model, X_poly, y, cv=10,
                                    scoring='r2')
    avg_cv_R = np.mean(cv_result_R)


    print(f'교차검증 RMSE: {cv_rmse}')
    print(f'교차검증 평균 RMSE: {avg_cv_rmse}')
    print(f'교차검증 표준편차 RMSE: {std_cv_rmse}')
    print(f'교차검증 R^2: {cv_result_R}')
    print(f'교차검증 평균 R^2: {avg_cv_R}')

    # 교차검증 예측값 생성
    y_pred_cv = cross_val_predict(model, X_poly, y, cv=10)

    # 교차검증 RMSE 및 R^2 계산
    cv_pred_rmse = np.sqrt(mean_squared_error(y, y_pred_cv))
    cv_pred_r2 = r2_score(y, y_pred_cv)

    print(f'교차검증 예측값과실제값 RMSE: {cv_pred_rmse}')
    print(f'교차검증 예측값과실제값 R^2: {cv_pred_r2}')

    return


