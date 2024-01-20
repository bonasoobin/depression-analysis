
## 🚀 프로젝트명

### ✔️ 우울증 지수 예측 프로젝트 😞
<br>

## 📃 프로젝트 소개

#### ✔️ 이 프로젝트는 2018년부터 2022년까지의 전국 자치구 단위 데이터를 활용하여 <br> &nbsp; &nbsp; &nbsp; 우울증 지수를 예측하는 것을 목표로 합니다.
<br>

## 📋 목차
- [1. 기술 스택](#-기술-스택)
- [2. 문제 정의](#-문제-정의)
- [3. 팀원 소개 및 역할](#-팀원-소개-및-역할)
- [4. 프로젝트 진행 기록](#-프로젝트-진행-기록)
- [5. 데이터 소개](#-데이터-소개)
- [6. 데이터 전처리](#-데이터-전처리)
- [7. 탐색적 데이터 분석(EDA)](#-탐색적-데이터-분석eda)
- [8. 모델링](#-모델링)
- [9. 결론](#-결론)
- [10. 한계점](#-한계점)
<br>

## 🛠 기술 스택

### ▪ 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### ▪ 주요 라이브러리
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">  <img src="https://img.shields.io/badge/scikit learn-F7931E?style=for-the-badge&logo=scikit learn&logoColor=white">  <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/seaborn-99CC00?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/statsmodels-181717?style=for-the-badge&logo=statsmodels&logoColor=white">
<!--
<img src="https://img.shields.io/badge/wordcloud-FF4F8B?style=for-the-badge&logo=wordcloud&logoColor=white">
<img src="https://img.shields.io/badge/konlpy-FF0000?style=for-the-badge&logo=konlpy&logoColor=white"> <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=collections&logoColor=white">-->


### ▪ 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
### ▪ 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Google Slides&logoColor=white">
<br>
<br>

## ⚠️ 문제 정의

2022년 기준, 한국은 OECD 국가 중 우울증 유병률이 가장 높습니다.  
2003년부터 2016년, 그리고 2017년을 제외한 **18년 동안 OECD 국가 중 자살률은 1위를 기록했습니다.**    
통계청에 따르면 **자살 원인 중 우울증이 35.4%** 로 가장 큰 비율을 차지합니다.  
<br>
실제로 자살 관련 기사를 많이 접하고, 주변에서도 우울증으로 인해 병원을 찾는 사람들을 자주 볼 수 있습니다.   
국민건강보험공단에 따르면, 2020년 우울증 진료를 받은 인원은 100만 461명에 달합니다.   
국민 4명 중 1명이 정신 질환을 경험하지만, 정부의 정신건강 예산은 세계보건기구(WHO) 권장치의 절반에도 미치지 못합니다.   
<br>
이러한 배경을 바탕으로, 우울증 지수에 영향을 미치는 변수를 파악하고 이에 대한 정책적 해결책을 모색하기 위해 본 프로젝트를 기획하였습니다.  

<br>

## 👩🏻‍💻 팀원 소개 및 역할

### ✔️ 팀원
- [❤️ 공예림 ❤️](https://github.com/yelimkong)
- [💛 김란 💛](https://github.com/raneeKim)
- [💙 한수빈 💙](https://github.com/bonasoobin)

### ✔️ 역할 분담
프로젝트를 진행하며 모든 팀원이 머신러닝 프로세스에 대한 경험을 쌓기 위해 데이터 수집 및 전처리, 탐색적 데이터 분석(EDA), 모델링, 파라미터 튜닝, 그리고 인사이트 도출과 같은 다양한 단계들을 함께 수행했습니다. 
작업의 관리를 용이하게 하기 위해, 각 팀원의 이름을 사용하여 별도의 브랜치(yelim, ranee, soobin)를 만들어 기록했습니다. 
<br>

### ✔️ 담당 모델
- GradientBoost : 공예림   
- Polynomial Regression / Ridge: 김란  
- SVR / RandomForest: 한수빈  
<br>



## 📅 프로젝트 진행 기록

### ✔️ 수행 기간
2023.12.29 ~ 2024.01.18 (3주)

### ✔️ 세부 진행 기록
- 23-12-29 : 주제 정하기 및 가설 설정
- 24-01-02 : 데이터 수집 및 전처리  
- 24-01-04 : 데이터 전처리
- 24-01-07 : 데이터 전처리
- 24-01-11 : EDA
- 24-01-15 : 모델링
- 24-01-16 : 최종 모델 선정 및 결론 정리
- 24-01-18 : 깃허브 readme 작성 및 노션 정리
<br>


## 📊 데이터 소개
### ✔️ 원본 데이터
- 우울증 환자 수 &nbsp; [출처](https://www.data.go.kr/data/15118810/fileData.do)
- 평균연령 &nbsp; [출처](https://jumin.mois.go.kr/etcStatAvgAge.do)
- 총인구수 &nbsp; [출처](https://jumin.mois.go.kr/)
- 스트레스 인지율 &nbsp; [출처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1YL0000_1&vw_cd=MT_GTITLE02&list_id=11_21&obj_var_id=A&itm_id=11110&seqNo=&conn_path=MT_GTITLE02&path=%252FstatisticsList%252FstatisticsListIndex.do)
- 고용률 &nbsp; [출처](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1DA7004S&vw_cd=MT_ZTITLE&list_id=B11&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE)
- 코로나 확진자 수 &nbsp; [출처](https://www.data.go.kr/data/15124288/fileData.do)
- 인구 1인당 지역사회 정신건강 예산 &nbsp; [출처](https://kosis.kr/statHtml/statHtml.do?orgId=117&tblId=DT_920023_A010)
- 전국 도시 공원 정보 표준 데이터 &nbsp; [출처](https://www.data.go.kr/data/15012890/standard.do)
- 공공시설 운영 현황 &nbsp; [출처](https://www.lofin365.go.kr/portal/LF5110000.do?pdtaId=9YJWO8ESQV63PIUNS62Q1211398&rdIncrYn=Y&frstParamYn=Y)

### ✔️ 변수 선정 이유
여러 논문과 기사, 정부 기관에서 발표된 통계 결과들을 바탕으로 우울증의 발생과 관련이 있을 것으로 예상되는 **평균 연령, 총 인구 수, 스트레스 인지율, 고용률, 코로나 확진자 수, 1인당 정신건강 예산, 공공시설 개수**를 독립변수로 선택하여 분석에 활용하기로 결정하였습니다. <br>

### ✔️ 데이터 세부 사항
+ 기준 : 자치구 단위<br>
+ 데이터 기간 : 2018년 ~ 2022년
+ 데이터 개수 : 1250개<br>
1. 시도 <br>
2. 자치구 <br>
3. 행정번호 <br>
4. 년도 <br>
5. 우울증 환자 수<br>
6. 평균연령 <br>
7. 총인구수 <br>
8. 스트레스 인지율 <br>
9. 고용률 <br>
10. 코로나 확진자 수<br>
11. 1인당 정신건강 예산(원) <br>
12. 공공시설 개수 <br>
13. 우울증 지수  ----> 종속변수 <br>
<br>



## 💡 데이터 전처리
+ (1) `int`형이었던 행정번호 컬럼은 `object`형으로 형변환
+ (2) 2018년, 2019년의 코로나 확진자 수 0명으로 대체 
+ (3) 공공시설 데이터와 공원 데이터 자치구 단위로 통합(공원 데이터 내 묘지공원(기피시설) 제외)
+ (4) 공원 데이터는 2023년 기준 누적 데이터이므로 자치구명 변경된 데이터는 자체 수정(대구광역시 군위군 -> 경상북도 군위군)
+ (5) 시도, 자치구, 행정번호 컬럼은 식별자 컬럼이기 때문에 삭제 <br><br>
**결측값 처리**
+ (6-1) 서울, 부산, 대구, 인천, 광주, 대전, 울산 등 7개 광역시의 2018-2020년 자치구별 고용률 데이터 결측치는 시도 데이터로 대체 처리
+ (6-2) 1인당 정신건강 예산 데이터는 자치구별 정신건강 예산 데이터가 부재하여, 시도별 데이터로 대체 처리
+ (6-3) 세종특별자치시, 제주특별자치도의 5년간 스트레스 인지율 데이터는 시도 데이터로 대체 처리
+ (6-4) 공공시설 데이터 중 2021년 데이터 부재로 2020년과 2022년의 평균값으로 대체
<br>

## 💡 탐색적 데이터 분석(EDA)
+ (1) 변수 간 상관관계 행렬과 산점도 확인 → 선형관계가 없다는 것을 확인
+ (2) `VIF` 분석을 통한 다중공선성 확인 → **다중공선성 없는 것으로 확인**
+ (3) `boxplot`을 통해 이상치 확인 후, 이상치에 민감하지 않은 `RobustScaler`을 진행
+ (4) **`ACF` 그래프를 통해 년도 변수가 독립적임을 확인** → 년도 변수 삭제
+ (5) 종속변수를 이루는 변수인 우울증환자수 변수와 총인구수 변수 삭제 


  <p align="center"><img src="https://github.com/yelimkong/depression-analysis/assets/48948604/d5cccbb7-b31c-4f37-ac8c-a73d8b5745a4"></p>

raw 데이터에서 변수별 히스토그램을 그려보았을 때, 스트레스 인지율과 고용률 변수는 비교적 정규분포와 유사한 형태를 보이며, 평균 연령 변수는 비교적 균등하게 퍼져있으며 중앙값 주위에 집중된 모습을 보입니다. 다른 대부분의 변수들은 낮은 값에서 높은 빈도를 보이고 오른쪽으로 긴 꼬리를 가지고 있습니다. 
<br>
<br>

<p align="center"><img src="https://github.com/yelimkong/depression-analysis/assets/48948604/0b93b44f-3669-40b9-9d46-0d5464eddadb"></p>


변수 간의 상관관계를 분석한 결과, 우울증 지수와 우울증 환자 수는 강한 상관관계를, 우울증 지수와 고용률은 중간 정도의 음의 상관관계를 띄는 것을 확인할 수 있었습니다.
<br>
<br>

<p align="center"><img src="https://github.com/yelimkong/depression-analysis/assets/48948604/2f65e7e2-c1f5-4e28-bfed-a9f29e083e8c"></p>

독립변수들과 종속변수(우울증 지수)간의 산점도를 확인하였을때 모두 비선형관계를 보이고 있습니다.
<br>
<br>
<br>

<table class="tg">
<thead>
  <tr>
    <th class="tg-nbj5">VIF Factor</th>
    <th class="tg-nbj5">features</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-t1ow">5.39</td>
    <td class="tg-t1ow">총 인구 수</td>
  </tr>
  <tr>
    <td class="tg-c3ow">3.09</td>
    <td class="tg-c3ow">우울증 환자 수</td>
  </tr>
  <tr>
    <td class="tg-t1ow">2.72</td>
    <td class="tg-t1ow">평균 연령</td>
  </tr>
  <tr>
    <td class="tg-c3ow">2.26</td>
    <td class="tg-c3ow">공공시설 개수</td>
  </tr>
  <tr>
    <td class="tg-t1ow">1.88</td>
    <td class="tg-t1ow">고용률</td>
  </tr>
  <tr>
    <td class="tg-c3ow">1.44</td>
    <td class="tg-c3ow">코로나 확진자 수</td>
  </tr>
  <tr>
    <td class="tg-x2zk">1.32</td>
    <td class="tg-x2zk">1인당 정신건강 예산(원)</td>
  </tr>
  <tr>
    <td class="tg-c3ow">1.29</td>
    <td class="tg-c3ow">스트레스 인지율</td>
  </tr>
</tbody>
</table>
VIF 분석을 통해 다중공선성이 없음을 확인하였습니다.
<br>

<br>
<br>

## 💡 모델링
#### ✔️ 변수 간 비선형 관계임을 확인한 후 비선형 모델로 모델링

<table class="tg">
<thead>
  <tr>
    <th class="tg-y698" rowspan="2">알고리즘 모델</th>
    <th class="tg-y698" colspan="2">모델 성능 평가 지표</th>
    <th class="tg-y698" rowspan="2">비고</th>
  </tr>
  <tr>
    <th class="tg-y698">r²</th>
    <th class="tg-y698">rmse</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-y698">GradientBoost</td>
    <td class="tg-c6of">0.987</td>
    <td class="tg-c6of">0.131</td>
    <td class="tg-c6of">train/test</td>
  </tr>
  <tr>
    <td class="tg-y698">Polynomial Regression</td>
    <td class="tg-c6of">0.734</td>
    <td class="tg-c6of">0.626</td>
    <td class="tg-c6of">cross_validation (cv=10)</td>
  </tr>
  <tr>
    <td class="tg-y698">Ridge Polynomial Regression</td>
    <td class="tg-c6of">0.835</td>
    <td class="tg-c6of">0.492</td>
    <td class="tg-c6of">cross_validation (cv=10), alpha=1</td>
  </tr>
  <tr>
    <td class="tg-y698">SVR</td>
    <td class="tg-c6of">0.752</td>
    <td class="tg-c6of">0.458</td>
    <td class="tg-c6of">cross_validation (cv=5)</td>
  </tr>
  <tr>
    <td class="tg-y698">RandomForest</td>
    <td class="tg-c6of">0.983</td>
    <td class="tg-c6of">0.146</td>
    <td class="tg-c6of">cross_validation (cv=10)</td>
  </tr>
</tbody>
</table>

👉 성능 평가가 가장 높은 `GradientBoost` 로 최종 모델 선정
<br>
<br>

### ✔️ 결과 해석
<p align="center"><img src=https://github.com/yelimkong/depression-analysis/assets/48948604/5a0626d3-a6cc-4248-bb6a-d9457f8e963a></p>
<br>

#### [그래프 해석]
우울증 환자 수, 총 인구 수 변수가 우울증 지수를 예측하는 데 중요한 역할을 합니다.
<br>


<p align="center"><img src=https://github.com/yelimkong/depression-analysis/assets/48948604/325a6b32-3c07-4a89-bd8f-34a3a7e8e01a></p>
<br>
잔차의 등분산성 그래프를 그려보았을때, 잔차 플롯에서 어느 정도 0 주변에서 관측 되는, 기울기가 0인 빨간 선을 확인하였습니다. 이 중 몇개의 데이터는 이상치로 보이지만 0을 중심으로 특정한 패턴을 가지고 있지 않음을 확인할 수 있으며 잔차가 0을 중심으로 크게 벗어나지 않음을 확인할 수 있습니다.
<br>

## ✔️ 결론

<br>

## ✔️ 한계점

<br>


    

## 🔍 참고 자료

### ✔️ 논문
1) 고찬영, 2021, 다중선형회귀분석을 이용한 중고차 가격 예측 연구 : A사의 사례를 중심으로』, 인하대학교 물류전문대학원 석사학위 논문
2) Sümeyra MUTİ1, Kazım YILDIZ2, 2023, Using Linear Regression For Used Car Price Prediction
,International Journal of Computational and
Experimental Science and ENgineering
,Vol. 9-No.1 (2023) pp. 11-16
