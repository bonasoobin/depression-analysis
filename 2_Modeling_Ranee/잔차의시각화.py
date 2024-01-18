import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score


final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
# final['우울증지수'] = round((final['우울증환자수']/final['총인구수'])*100, 2) 
final.columns = ['city','neighborhood','citynum','year','patient','age','population','stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

from sklearn.model_selection import GridSearchCV


# 데이터를 train, test 세트로 분할 (7:3 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=23)

# RobustScaler 적용
scaler = RobustScaler()
X_scaled = scaler.transform(X)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)



# 그래디언트 부스팅 모델을 위한 하이퍼파라미터 그리드 정의
param_grid = {
    'n_estimators': [100, 200, 300],
    'learning_rate': [0.01, 0.05, 0.1],
    'max_depth': [3, 4, 5],
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2, 3],
    'subsample': [0.8, 0.9, 1.0]
}

# 그리드 서치 객체 생성
grid_search = GridSearchCV(GradientBoostingRegressor(random_state=0), param_grid, cv=5, scoring='r2', n_jobs=-1, verbose=2)

'''
cv=5: 5-폴드 교차 검증을 의미
scoring='r2':  R² 점수를 사용합니다.
n_jobs=-1: 가능한 모든 CPU 코어를 사용하여 계산을 가속화
verbose=2: 진행 상황에 대한 자세한 출력을 제공
'''

# 그리드 서치 실행
grid_search.fit(X_train_scaled, y_train)

# 최적의 매개변수와 점수 출력
best_params = grid_search.best_params_
best_score = grid_search.best_score_

best_params, best_score

# 그리드 서치 결과를 반영한 최적의 매개변수 사용
optimal_params = {
    'learning_rate': 0.1,
    'max_depth': 4,
    'min_samples_leaf': 1,
    'min_samples_split': 6,
    'n_estimators': 300,
    'subsample': 0.8
}

gb_model = ()
# 그래디언트 부스트 모델 생성 및 훈련
gb_model = GradientBoostingRegressor(**optimal_params, random_state=123)
gb_model.fit(X_train_scaled, y_train)


'''
성능 평가
RMSE : 모델의 예측 정확도를 평가
MSE : MSE는 실제 값과 예측 값 간의 차이의 제곱 평균
R² Score : 결정 계수(R² 점수)를 계산, 모델이 데이터의 변동성을 얼마나 잘 설명함
'''


# 예측 및 성능 평가
y_pred_gb = gb_model.predict(X_test_scaled)
mse_gb = mean_squared_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print("Test - RMSE:", rmse_gb, "MSE:", mse_gb, "R2 Score:", r2_gb)

# Train 세트에 대한 예측 및 평가
y_pred_train = gb_model.predict(X_train_scaled)
mse_train = mean_squared_error(y_train, y_pred_train)
rmse_train = np.sqrt(mse_train)
r2_train = r2_score(y_train, y_pred_train)

print("Train - RMSE:", rmse_train, "MSE:", mse_train, "R2 Score:", r2_train)


import seaborn as sns
import matplotlib.pyplot as plt

# Test 세트에 대한 예측 및 잔차 계산
y_pred_test = gb_model.predict(X_test_scaled)
residuals_test = y_test - y_pred_test


y_all = gb_model.predict(X_scaled)
residuals_all = y - y_all


# 잔차 플롯
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_all, y=residuals_all)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.title('Residual Plot (All Data)')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')


# Q-Q plot 그리기 (정규성확인)
import statsmodels.api as sm

sm.qqplot(residuals_all, line='s', fit=True)
plt.title('Q-Q Plot of Residuals')
plt.show()