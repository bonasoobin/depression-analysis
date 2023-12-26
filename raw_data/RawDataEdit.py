import pandas as pd

a = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\서울특별시.csv', encoding='ANSI')
b = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\부산광역시.csv', encoding='ANSI')
c = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\대구광역시.csv', encoding='ANSI')
d = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\인천광역시.csv', encoding='ANSI')
e = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\광주광역시.csv', encoding='ANSI')
f = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\대전광역시.csv', encoding='ANSI')
g = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\울산광역시.csv', encoding='ANSI')
h = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\세종특별자치시.csv', encoding='ANSI')
i = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\경기도.csv', encoding='ANSI')
j = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\강원특별자치도.csv', encoding='ANSI')
k = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\충청북도.csv', encoding='ANSI')
l = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\충청남도.csv', encoding='ANSI')
m = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\전라북도.csv', encoding='ANSI')
n = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\전라남도.csv', encoding='ANSI')
o = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\경상북도.csv', encoding='ANSI')
p = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\경상남도.csv', encoding='ANSI')
q = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\평균연령\\제주특별자치도.csv', encoding='ANSI')

seoul = a.drop(0)
busan = b.drop(0)
daegu = c.drop(0)
incheon = d.drop(0)
gwangju = e.drop(0)
dageon = f.drop(0)
ulsan = g.drop(0)
sejong = h.drop(0)
gyeonggi = i.drop(0)
gangwon = j.drop(0)
choongbuk = k.drop(0)
choongnam = l.drop(0)
jeonbuk = m.drop(0)
jeonnam = n.drop(0)
gyeonbuk = o.drop(0)
gyeonnam = p.drop(0)
jeju = q

result = pd.concat([seoul,busan,daegu,incheon,gwangju,dageon,ulsan,sejong,gyeonggi,gangwon,choongbuk,choongnam,jeonbuk,jeonnam,gyeonbuk,gyeonnam,jeju])

result.to_csv("평균연령.csv", encoding = 'ANSI')

# 병합한 csv 파일 정렬 및 편집

merged_csv = pd.read_csv('C:\\Users\\MSI\\Desktop\\depression-project\\Ranee\\raw_data\\연령,스트레스인지율병합.csv', encoding='ANSI')



age = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\age&stress.csv', encoding='ANSI')
population = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\population&employment.csv', encoding='ANSI')
others = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\0_Data\others.csv', encoding='ANSI')
default_index = pd.read_csv(r'C:\Users\MSI\Desktop\depression-project\Ranee\raw_data\지자체구분.csv', encoding = 'ANSI')

age.info
age.isnull()
population.info
population = population.drop(['시도','시군구'], axis='columns')
others.info
others.isnull()
others = others.drop(['시도','시군구'], axis='columns')
default_index = default_index.drop(['Unnamed: 3','Unnamed: 4'],axis=1)
a = pd.merge(default_index,age, on='행정번호')
b = pd.merge(a,population, on=['행정번호','년도'])
final_data = pd.merge(b,others, on=['행정번호','년도'])
final_data.to_csv("final.csv", encoding = 'ANSI')

