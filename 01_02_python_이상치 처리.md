## 이상치

### IQR 이상치 감지
```
import pandas as pd

def detect_outliers(df, column_name):

    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
    
    return outliers
```
### IQR 이상치 감지 및 처리 클래스
```
import pandas as pd

class OutlierDetector:
    def __init__(self, df, column_name):
   
        self.df = df
        self.column_name = column_name
        self.lower_bound = None
        self.upper_bound = None
    
    def calculate_iqr(self):

        Q1 = self.df[self.column_name].quantile(0.25)
        Q3 = self.df[self.column_name].quantile(0.75)
        IQR = Q3 - Q1
        self.lower_bound = Q1 - 1.5 * IQR
        self.upper_bound = Q3 + 1.5 * IQR
    
    def detect_outliers(self):

        if self.lower_bound is None or self.upper_bound is None:
            self.calculate_iqr()
        outliers = self.df[(self.df[self.column_name] < self.lower_bound) | 
                           (self.df[self.column_name] > self.upper_bound)]
        return outliers
    
    def remove_outliers(self):

        if self.lower_bound is None or self.upper_bound is None:
            self.calculate_iqr()
        df_no_outliers = self.df[(self.df[self.column_name] >= self.lower_bound) & 
                                  (self.df[self.column_name] <= self.upper_bound)]
        return df_no_outliers
    
    def replace_outliers_with_mean(self):

        if self.lower_bound is None or self.upper_bound is None:
            self.calculate_iqr()
        mean_value = self.df[self.column_name].mean()
        self.df[self.column_name] = self.df[self.column_name].apply(
            lambda x: mean_value if x < self.lower_bound or x > self.upper_bound else x
        )
        return self.df

```
사용 예시
```
df = pd.DataFrame({'column_name': [your_data_here]})
```
```
detector = OutlierDetector(df, 'column_name')
```
```
outliers = detector.detect_outliers()
```
```
df_no_outliers = detector.remove_outliers()
```
```
df_with_mean_replaced = detector.replace_outliers_with_mean()
```

mean_v = df['01'].mean()
df['01'] = df['01'].appy(lambda x: mean_v if x <lower_bound or x > upper_bound else x)

### 이상치 제거
df_no_outliers = df[(df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound)]

### 이상치를 평균값으로 대체
mean_value = df['column_name'].mean()
df['column_name'] = df['column_name'].apply(lambda x: mean_value if x < lower_bound or x > upper_bound else x)

## 데이터 변환

### 특정 열의 데이터 타입을 정수형으로 변환
df['column_name'] = df['column_name'].astype(int)

### 특정 열의 데이터 타입을 문자열로 변환
df['column_name'] = df['column_name'].astype(str)

### 특정 열의 데이터 타입을 부동 소수점으로 변환
df['column_name'] = df['column_name'].astype(float)

## 인코딩(원핫인코딩?)
```
df_encoded = pd.get_dummies(df, columns=['category_column'])
```
   id category_column  value
0  1              A     10
1  2              B     15
2  3              A     10
3  4              C     20

   id  value  category_column_A  category_column_B  category_column_C
0  1     10                  1                  0                  0
1  2     15                  0                  1                  0
2  3     10                  1                  0                  0
3  4     20                  0                  0                  1

## 샘플링
```
### 데이터셋에서 50% 샘플 추출
df_sampled = df.sample(frac=0.5)

### 데이터셋에서 100개의 샘플 추출
df_sampled_n = df.sample(n=100)
```
frac=0.5를 사용하면 전체 데이터의 비율에 따라 샘플을 추출하고, n=100을 사용하면 원하는 개수만큼 샘플을 선택합니다. 두 방법 모두 데이터 분석이나 모델링에서 데이터의 일부를 랜덤하게 선택할 때 유용하게 사용됩니다.

## 특징 선택 및 추출
### 선택
```
from sklearn.feature_selection import SelectKBest, f_classif

# 특징 선택 (상위 5개의 특징 선택)
selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X, y)

# 선택된 특징의 인덱스
selected_features = selector.get_support(indices=True)
print(selected_features)
```
#### 추출
```
# 두 열의 곱을 새로운 특징으로 추가
df['new_feature'] = df['feature1'] * df['feature2']

# 두 열의 합을 새로운 특징으로 추가
df['new_feature_sum'] = df['feature1'] + df['feature2']
```