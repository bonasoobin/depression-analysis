from sklearn.model_selection import GridSearchCV, cross_val_score, cross_val_predict
from sklearn.linear_model import Ridge
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# 데이터셋 로딩

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final.columns = ['city','neighborhood','citynum','year','patient','age','population',
                 'stress','employment','covid','budget','public facilities','depression']

X = final[['patient','age','population','stress','employment','covid','budget',
           'public facilities']]
y = final['depression']

# 독립 변수와 종속 변수 설정
X = final[['patient', 'age', 'population', 'stress', 'employment', 'covid', 'budget', 'public facilities']]
y = final['depression']

# 파이프라인 구성
pipeline = Pipeline([
    ('scaler', RobustScaler()),  # 로버스트 스케일러
    ('ridge', Ridge())           # 릿지 회귀 모델
])

# 그리드 서치를 위한 매개변수 그리드
param_grid = {
    'ridge__alpha': [0.1, 1, 10, 100]  # 알맞게 조정 가능한 alpha 값 리스트
}

# 그리드 서치 객체 생성
grid_search = GridSearchCV(pipeline, param_grid, scoring='neg_mean_squared_error', cv=10)

# 그리드 서치 수행
grid_search.fit(X, y)

# 최적의 하이퍼파라미터
best_alpha = grid_search.best_params_['ridge__alpha']

print(f'최적의 alpha: {best_alpha}')

# 최적의 모델 획득
best_model = grid_search.best_estimator_

# 교차검증 예측값 생성
y_pred_cv = cross_val_predict(best_model, X, y, cv=10)

# 교차검증 RMSE 및 R^2 계산
cv_pred_rmse = np.sqrt(mean_squared_error(y, y_pred_cv))
cv_pred_r2 = r2_score(y, y_pred_cv)

print(f'교차검증 예측값과 실제값 RMSE: {cv_pred_rmse}')
print(f'교차검증 예측값과 실제값 R^2: {cv_pred_r2}')
