import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final(preprocessing).csv', encoding='utf-8', index_col=0)
final.info()


age = final['age']
population = final['population']
stress = final['stress']
employment = final['employment']
covid = final['covid']
budget = final['budget']
pf = final['public facilities']
depression = final['depression']

# 상관관계계수 확인 및 시각화
final_corr = final[['age','population','stress','employment','covid','budget','public facilities','depression']]
corr_df = final_corr.corr()
ax = sns.heatmap(corr_df())
plt.show()




import pingouin as pg 
# pip install seaborn pingouin pandas 
pg.normality(depression)

