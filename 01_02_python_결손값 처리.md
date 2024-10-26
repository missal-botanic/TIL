
결손값 확인 및 처리
=============

### DATA 확인
df.head()  # 첫 5행을 확인
df.shape  # (행의 수, 열의 수)
df.columns  # 컬럼명 리스트
df.dtypes  # 각 컬럼의 데이터 타입
df.describe()  # 수치형 데이터의 요약 통계량
df.info()  # 전체적인 데이터 프레임 정보
df.sample(n=5)  # 랜덤으로 5행 선택
df['컬럼명'].unique()  # 특정 컬럼의 고유 값 리스트

### 결손값 확인
print(df.isnull().sum())

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

### 결측값 대체 fillna()
```py
df_filled = df.fillna(0) # 결측값을 0으로 대체
df_filled_mean = df.fillna(df.mean()) # 결측값을 각 열의 평균값으로 대체
df_filled_median = df.fillna(df.median()) # 결측값을 각 열의 중간값으로 대체
df_filled_mode = df.fillna(df.mode().iloc[0]) # 결측값을 각 열의 최빈값으로 대체
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

