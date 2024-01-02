import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import statsmodels.api as sm

final = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\final.csv', encoding='ANSI')
final.info()
final['우울증지수'] = round((final['우울증환자수']/final['총인구수'])*100, 2) 
final.columns = ['city','neighborhood','citynum','year','patient','age','population','stress','employment','covid','budget','public facilities','depression']


def acf_cheak(city,name) :
    acf_array = final[final['citynum'] == city]
    data = np.array(acf_array[f"{name}"])


    time_series = pd.Series(data, index=pd.to_datetime(acf_array['year'],format='%Y'))

    acf_result = sm.tsa.acf(time_series, nlags=len(acf_array['year'])-1)

    plt.stem(range(1, len(acf_array['year'])), acf_result[1:])
    plt.xlabel('Lag')
    plt.ylabel('Auto correlation')
    plt.title('ACF')
    plt.savefig(f"{city}의{name}")
    plt.close()


citynum =final[final['citynum'] >= 4211000000]['citynum']
index_name = ['age','population','stress','employment','covid','budget','public facilities','depression']

for i in citynum :
    for e in index_name :
        acf_cheak(i,e)

