
결손값 확인 및 처리
=============

### DATA 확인
```py
df.head()  # 첫 5행을 확인
df.shape  # (행의 수, 열의 수)
df.columns  # 컬럼명 리스트
df.dtypes  # 각 컬럼의 데이터 타입
df.describe()  # 수치형 데이터의 요약 통계량
df.info()  # 전체적인 데이터 프레임 정보
df.sample(n=5)  # 랜덤으로 5행 선택
df['컬럼명'].unique()  # 특정 컬럼의 고유 값 리스트
```

### 결손값 확인
```py
print(df.isnull().sum())
```

------------

### 결손값 제거

### 모든 결손값이 있는 행 삭제:

```py
df = df.dropna()  

```

------------

### 결손값 대체

```py
df['column_name'] = df['column_name'].fillna(0) # 결손값을 0으로 대체
```

```py
df['column_name'] = df['column_name'].fillna(df['column_name'].mode()[0]) # 최빈값(most frequent value)으로 대체  
```

```py
df['column_name'] = df['column_name'].fillna(df['column_name'].median()) # 중앙값(median)으로 대체 
```

```py
df['column_name'] = df['column_name'].fillna(df['column_name'].mean()) # 평균값(mean)으로 대체 
```

## 결측값 제거 dropna()
```py
df_dropped_rows = df.dropna() # 결측값이 포함된 행 제거
df_dropped_cols = df.dropna(axis=1) # 결측값이 포함된 열 제거
```
------------

### 카테고리형 변수의 결손값 처리

```py
df['category_column'] = df['category_column'].fillna('Unknown') # 가장 빈번한 카테고리로 대체. 새로운 카테고리(예: "Unknown")를 추가하여 대체
```

### 특정 전략을 이용한 대체

```py
df['column_name'] = df.groupby('group_column')['column_name'].transform(lambda x: x.fillna(x.mean())) #그룹별 평균으로 대체
```

### 특정 열에서 결손값이 있는 행 삭제:

```py
df = df.dropna(subset=['column_name'])

```

------------

### 데이터 변환
결손값을 포함한 새로운 변수를 생성: 결손값이 있는지를 나타내는 새로운 이진 변수(0/1)를 생성할 수 있습니다.
```py
df['column_name_is_null'] = df['column_name'].isnull().astype(int)  # 결손값이 있는지 여부'''를 나타내는 변수 생성
```

### 데이터 보간(interpolation)

```py
df['column_name'] = df['column_name'].interpolate() #선형 보간: 수치형 데이터의 결손값을 인접한 값들로 보간하여 대체합니다.
```

------------

### ML으로 결손값 채우기

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import random

# 랜덤 시드 설정
random_seed = random.randint(0, 99999)
np.random.seed(random_seed)

# 데이터 생성
data = {'fe1': np.random.rand(100), 'cwn': np.random.rand(100)}
data['cwn'][::10] = np.nan  # NaN 값 추가
df = pd.DataFrame(data)

# NaN이 아닌 데이터 분리
df_wnn = df[df['cwn'].notnull()]

# 모델 학습
model = LinearRegression()
X = df_wnn['fe1'].values.reshape(-1, 1)  # 2D로 변형
y = df_wnn['cwn'].values
model.fit(X, y)

# NaN인 데이터 예측
df_wn = df[df['cwn'].isnull()]
predictions = model.predict(df_wn['fe1'].values.reshape(-1, 1))

# 결과 출력
df_wn['cwn'] = predictions  # 예측 결과를 추가
result = pd.concat([df_wnn, df_wn], ignore_index=True)  # 원본 데이터와 예측 결과 합치기

# 원본 데이터와 예측 결과 비교
print(result[['fe1', 'cwn']])
