import pandas as pd
import numpy as np

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



import pingouin as pg 
# pip install seaborn pingouin pandas 
pg.normality(depression)



