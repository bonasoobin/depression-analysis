import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
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

def poly_regression(num) :
    poly = PolynomialFeatures(degree=num)
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


    # 훈련 데이터에 대한 산점도와 회귀선
    plt.figure(figsize=(12, 6))
    plt.scatter(y_train, y_train_pred, color='blue', label='Training Data')
    plt.plot([min(y_train), max(y_train)], [min(y_train), max(y_train)], linestyle='--', color='red', linewidth=2, label='Ideal Line')
    plt.title('Training Data: Actual vs Predicted')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.legend()
    plt.show()

    # 테스트 데이터에 대한 산점도와 회귀선
    plt.figure(figsize=(12, 6))
    plt.scatter(y_test, y_test_pred, color='green', label='Test Data')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2, label='Ideal Line')
    plt.title('Test Data: Actual vs Predicted')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.legend()
    plt.show()

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

# 릿지회귀로 규제주기 (모든 특성이 중요하거나 특성관 상관관계가 높은 경우)
from sklearn.linear_model import Ridge 

def ridge_poly_regression(num) :
    
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

# 교차검증 사용
from sklearn.model_selection import cross_val_score
X_robust = robust_scaler.fit_transform(X) 

def cross_poly_regression(num) :
    poly = PolynomialFeatures(degree=num)
    X_poly = poly.fit_transform(X_robust)

    model = LinearRegression()

    # rmse
    cv_result_rmse = cross_val_score(model, X_poly, y, cv=10,
                                     scoring='neg_mean_squared_error')
    cv_rmse = np.sqrt(-cv_result_rmse) # 음수의 평균 제곱 오차를 양수로 변환
    average_cv_rmse = np.mean(cv_rmse)

    # R^2
    cv_result_R = cross_val_score(model, X_poly, y, cv=10,
                                     scoring='r2')
    average_cv_R = np.mean(cv_result_R)

    print(f'교차검증 RMSE: {cv_rmse}')
    print(f'교차검증 평균 RMSE: {average_cv_rmse}')
    print(f'교차검증 R^2: {cv_result_R}')
    print(f'교차검증 평균 R^2: {average_cv_R}')

    return

cross_poly_regression(2) # cv = 5 -> 완전 별로
'''
교차검증 RMSE: [ 0.39350687  0.47593173  0.62255396  0.4599823  48.70644689]     
교차검증 평균 RMSE: 10.131684349977695
교차검증 R^2: [ 8.93991681e-01  8.33854313e-01  7.03512143e-01  8.56342161e-01   
                -1.41367994e+03]
교차검증 평균 R^2: -282.07844796580486      
'''

cross_poly_regression(2) # cv = 10 -> 현재 모든 결과 중에 제일 좋음
'''
교차검증 RMSE: [0.41958439 0.39116508 0.53181487 0.40088593 0.71050097 0.38357998
 0.66904521 0.44761713 1.24855768 0.53685742]
교차검증 평균 RMSE: 0.5739608660306115
교차검증 R^2: [0.91029439 0.76714191 0.83540047 0.7599392  0.68057878 0.78868871
 0.73879823 0.74864692 0.18152806 0.66615522]
교차검증 평균 R^2: 0.7077171883468395
'''

def ridge_cross_poly_regression(num) :
    poly = PolynomialFeatures(degree=num)
    X_poly = poly.fit_transform(X_robust)    
    
    for a in [0,0.1,1] :

        model = Ridge(alpha=a)

        # rmse
        cv_result_rmse = cross_val_score(model, X_poly, y, cv=10,
                                        scoring='neg_mean_squared_error')
        cv_rmse = np.sqrt(-cv_result_rmse) # 음수의 평균 제곱 오차를 양수로 변환
        average_cv_rmse = np.mean(cv_rmse)

        # R^2
        cv_result_R = cross_val_score(model, X_poly, y, cv=10,
                                        scoring='r2')
        average_cv_R = np.mean(cv_result_R)

        #print(f'규제가 {a}일 때 교차검증 RMSE: {cv_rmse}')
        print(f'규제가 {a}일 때 교차검증 평균 RMSE: {average_cv_rmse}')
        #print(f'규제가 {a}일 때 교차검증 R^2: {cv_result_R}')
        print(f'규제가 {a}일 때 교차검증 평균 R^2: {average_cv_R}')

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