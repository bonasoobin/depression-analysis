import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor # 다중공산성

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.columns =  ['city','neighborhood','citynum','year','patient','age','population','stress','employment','covid','budget','public facilities','depression']
final.info()

fianl_dummy = pd.get_dummies(final, columns=['city']) # 

# 다중공산성 확인

independent_vairables = final[['age','population','stress','employment','covid','budget','public facilities']]
vif = pd.DataFrame
independent_vairables.columns
vif['feature'] = ['age','population','stress','employment','covid','budget','public facilities']
vif['VIF'] = [variance_inflation_factor(independent_vairables, i) for i in range(len(independent_vairables.columns))]