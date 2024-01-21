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


final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final.columns = ['city','neighborhood','citynum','year','patient','age','population',
                 'stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

robust_scaler = RobustScaler()

# 릿지회귀로 규제주기 (모든 특성이 중요하거나 특성관 상관관계가 높은 경우) -> 많을때 기여도 줄이고, 적은 변수는 올리고
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
    
    result2 = []
    for b in [5,10] :
        result = []
        for a in [0,0.1,1] :

            model = Ridge(alpha=a)

            # rmse
            cv_result_rmse = cross_val_score(model, X_poly, y, cv=b,
                                            scoring='neg_mean_squared_error')
            cv_rmse = np.sqrt(-cv_result_rmse) # 음수의 평균 제곱 오차를 양수로 변환
            avg_cv_rmse = np.mean(cv_rmse)
            std_cv_rmse = np.std(cv_rmse)

            # R^2
            cv_result_R = cross_val_score(model, X_poly, y, cv=b,
                                            scoring='r2')
            avg_cv_R = np.mean(cv_result_R)

            print(f'규제가 {a}일 때 교차검증 RMSE: {cv_rmse}')
            print(f'규제가 {a}일 때 교차검증 평균 RMSE: {avg_cv_rmse}')
            print(f'교차검증 표준편차 RMSE: {std_cv_rmse}')
            print(f'규제가 {a}일 때 교차검증 R^2: {cv_result_R}')
            print(f'규제가 {a}일 때 교차검증 평균 R^2: {avg_cv_R}')

            # 교차검증 예측값 생성
            y_pred_cv = cross_val_predict(model, X_poly, y, cv=b)

            # 교차검증 RMSE 및 R^2 계산
            cv_pred_rmse = np.sqrt(mean_squared_error(y, y_pred_cv))
            cv_pred_r2 = r2_score(y, y_pred_cv)

            print(f'교차검증 예측값 RMSE: {cv_pred_rmse}')
            print(f'교차검증 예측값 R^2: {cv_pred_r2}')
            result.append([avg_cv_rmse,avg_cv_R])
        result2.append(result)

    return result2

ridge_cross_poly_regression(2)

'''
규제가 0일 때 교차검증 RMSE: [ 0.37823952  0.36249484  0.36403249  0.3594387  47.59058531]
규제가 0일 때 교차검증 평균 RMSE: 9.810958173360678
교차검증 표준편차 RMSE: 18.889814674389307
규제가 0일 때 교차검증 R^2: [ 9.02057968e-01  9.03616340e-01  8.98624453e-01  9.12280373e-01
 -1.34960200e+03]
규제가 0일 때 교차검증 평균 R^2: -269.1970846784833
교차검증 예측값 RMSE: 21.28567590451866
교차검증 예측값 R^2: -306.13820677909484
규제가 0.1일 때 교차검증 RMSE: [ 0.37864468  0.36061052  0.36257384  0.36009538 54.9092132 ]
규제가 0.1일 때 교차검증 평균 RMSE: 11.274227524920871
교차검증 표준편차 RMSE: 21.817493913673292
규제가 0.1일 때 교차검증 R^2: [ 9.01848031e-01  9.04615781e-01  8.99435234e-01  9.11959559e-01
 -1.79694225e+03]
규제가 0.1일 때 교차검증 평균 R^2: -358.6648786067556
교차검증 예측값 RMSE: 24.558323374303356
교차검증 예측값 R^2: -407.8428255609105
규제가 1일 때 교차검증 RMSE: [ 0.38207203  0.36231776  0.36617434  0.36358828 93.29158214]
규제가 1일 때 교차검증 평균 RMSE: 18.95314690946271
교차검증 표준편차 RMSE: 37.169218292703775
규제가 1일 때 교차검증 R^2: [ 9.00063117e-01  9.03710489e-01  8.97428021e-01  9.10243307e-01
 -5.18903413e+03]
규제가 1일 때 교차검증 평균 R^2: -1037.0845368758369
교차검증 예측값 RMSE: 41.722566630809524
교차검증 예측값 R^2: -1179.0515713157088
규제가 0일 때 교차검증 RMSE: [0.41954495 0.33852369 0.42141049 0.30880438 0.41762571 0.32373241
 0.41148481 0.32016504 1.14255739 0.3986267 ]
규제가 0일 때 교차검증 평균 RMSE: 0.45024755594344634
교차검증 표준편차 RMSE: 0.23488603905673472
규제가 0일 때 교차검증 R^2: [0.91031126 0.82559887 0.89664814 0.85755523 0.88964071 0.84948382
 0.90119639 0.87140661 0.31460234 0.81593999]
규제가 0일 때 교차검증 평균 R^2: 0.8132383348195557
교차검증 예측값 RMSE: 0.5078329577497003
교차검증 예측값 R^2: 0.8251761343441317
규제가 0.1일 때 교차검증 RMSE: [0.41994909 0.3388111  0.41622802 0.30998955 0.41247972 0.3251529
 0.41100289 0.32196106 1.14131157 0.39906328]
규제가 0.1일 때 교차검증 평균 RMSE: 0.4495949176697528
교차검증 표준편차 RMSE: 0.23439782650402327
규제가 0.1일 때 교차검증 R^2: [0.91013838 0.8253026  0.89917453 0.85645974 0.89234366 0.84816003
 0.90142769 0.86995983 0.3160962  0.8155366 ]
규제가 0.1일 때 교차검증 평균 R^2: 0.8134599268789694
교차검증 예측값 RMSE: 0.507028530818811
교차검증 예측값 R^2: 0.8257295511300703
규제가 1일 때 교차검증 RMSE: [0.42732463 0.33813131 0.41789662 0.31029816 0.41677946 0.32512226
 0.41154171 0.32760505 1.06879929 0.39813015]
규제가 1일 때 교차검증 평균 RMSE: 0.44416286320900944
교차검증 표준편차 RMSE: 0.21260196259597594
규제가 1일 때 교차검증 R^2: [0.9069542  0.82600293 0.89836452 0.85617379 0.89008751 0.84818865
 0.90116907 0.86536065 0.40023808 0.81639825]
규제가 1일 때 교차검증 평균 R^2: 0.82089376469293
교차검증 예측값 RMSE: 0.492422830049223
교차검증 예측값 R^2: 0.8356251712807492
[[[9.810958173360678, -269.1970846784833], [11.274227524920871, -358.6648786067556], [18.95314690946271, -1037.0845368758369]],
 [[0.45024755594344634, 0.8132383348195557], [0.4495949176697528, 0.8134599268789694], [0.44416286320900944, 0.82089376469293]]] 
'''

import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def ridge_cross_poly_regression_visual(num) :
    poly = PolynomialFeatures(degree=num)
    X_robust = robust_scaler.fit_transform(X)
    X_poly = poly.fit_transform(X_robust)    

    model = Ridge(alpha=1)

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

    # 교차검증 예측값 생성
    y_pred_cv = cross_val_predict(model, X_poly, y, cv=10)

    # 교차검증 RMSE 및 R^2 계산
    cv_pred_rmse = np.sqrt(mean_squared_error(y, y_pred_cv))
    cv_pred_r2 = r2_score(y, y_pred_cv)

    residuals_all = y - y_pred_cv


    # 잔차 플롯
    #plt.subplot(1, 2, 1)
    sns.scatterplot(x=y, y=residuals_all)
    plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
    plt.title('Residual Plot (All Data)')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.show()


    # Q-Q plot 그리기 (정규성확인)
    

    sm.qqplot(residuals_all, line='s', fit=True)
    plt.title('Q-Q Plot of Residuals')
    plt.show()

    return

ridge_cross_poly_regression_visual(2)


