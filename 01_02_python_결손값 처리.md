df.head()
df.sample(n=5)

df.describe()



## 결손값 확인
print(df.isnull().sum())

## 결손값 대처 대표
df = df.dropna()
df['content'] = df['content'].fillna(df['content'].mode()[0]) #최반값
df['age'] = df['age'].fillna(df['age'].median()) #중앙값


## 결손값 제거

### 모든 결손값이 있는 행 삭제:

```
df = df.dropna()  

```

### 특정 열에서 결손값이 있는 행 삭제:

```
df = df.dropna(subset=['column_name'])

```


## 결손값 대체


### 결손값을 0으로 대체
```
df['column_name'] = df['column_name'].fillna(0) 
```

### 최빈값(most frequent value)으로 대체
```
df['column_name'] = df['column_name'].fillna(df['column_name'].mode()[0])  
```

### 중앙값(median)으로 대체
```
df['column_name'] = df['column_name'].fillna(df['column_name'].median())  
```

### 평균값(mean)으로 대체
```
df['column_name'] = df['column_name'].fillna(df['column_name'].mean())  
```

### 카테고리형 변수의 결손값 처리
가장 빈번한 카테고리로 대체.
새로운 카테고리(예: "Unknown")를 추가하여 대체

```
df['category_column'] = df['category_column'].fillna('Unknown')
```

### 특정 전략을 이용한 대체
그룹별 평균으로 대체
```
df['column_name'] = df.groupby('group_column')['column_name'].transform(lambda x: x.fillna(x.mean())) 
```

### 데이터 변환
결손값을 포함한 새로운 변수를 생성: 결손값이 있는지를 나타내는 새로운 이진 변수(0/1)를 생성할 수 있습니다.
```
df['column_name_is_null'] = df['column_name'].isnull().astype(int)  # 결손값이 있는지 여부'''를 나타내는 변수 생성
```

### 데이터 보간(interpolation)
선형 보간: 수치형 데이터의 결손값을 인접한 값들로 보간하여 대체합니다.
```
df['column_name'] = df['column_name'].interpolate()  
```

