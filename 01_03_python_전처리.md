결측값 처리 : 누락된 값
이상값 처리 : 비상식적으로 큰 값이나 작은 값
중복 데이터 제거 : 동일한 테이터 
데이터 타입 변환 : 데이터 타입 변환
데이터 정규화 : 범위를 일정하게
인코딩 : 범주형을 수치형으로
샘플링 : 데이터 셋의 크기를 줄이거나 늘리기
특징 선택 및 추출 : 중요한 특징 선택 및 새로운 특징 추출

### 1차원 배열 생성
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

### 2차원 배열 합치기
data = np.column_stack((A_x, A_y))

### 배열을 10x1 형태로 재구성
```
reshaped_arr = arr.reshape(-1, 1) #Pandas 2차원화
.values.reshape(-1, 1) #NumPy 2차원화


```

[[ 1]
 [ 2]
 [ 3]
 [ 4]
 [ 5]
 [ 6]
 [ 7]
 [ 8]
 [ 9]
 [10]]

## 결측값 제거 dropna()

```
df_dropped_rows = df.dropna() # 결측값이 포함된 행 제거
df_dropped_cols = df.dropna(axis=1) # 결측값이 포함된 열 제거
```

### 결측값 대체 fillna()
```
df_filled = df.fillna(0) # 결측값을 0으로 대체
df_filled_mean = df.fillna(df.mean()) # 결측값을 각 열의 평균값으로 대체
df_filled_median = df.fillna(df.median()) # 결측값을 각 열의 중간값으로 대체
df_filled_mode = df.fillna(df.mode().iloc[0]) # 결측값을 각 열의 최빈값으로 대체
```

### 성별과 탑승한 곳 인코딩
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic['embarked'] = titanic['embarked'].map({'C': 0, 'Q': 1, 'S': 2})

### 특성과 타겟 분리
X = titanic.drop('survived', axis=1)
y = titanic['survived']

### 필요한 열 선택 및 결측값 처리
data = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]


### 결측값 예측 LinearRegression() 
```
from sklearn.linear_model import LinearRegression

# 결측값이 있는 열과 없는 열 분리
df_with_na = df[df['column_with_na'].isnull()]
df_without_na = df[df['column_with_na'].notnull()]

# 회귀 모델 학습
model = LinearRegression()
model.fit(df_without_na[['feature1', 'feature2']], df_without_na['column_with_na'])

# 결측값 예측
predicted_values = model.predict(df_with_na[['feature1', 'feature2']])

# 예측된 값으로 결측값 대체
df.loc[df['column_with_na'].isnull(), 'column_with_na'] = predicted_values

```
예제
```
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 랜덤 시드를 설정하여 결과를 재현 가능하게 함
np.random.seed(42)

# 샘플 데이터 생성
data = {
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'column_with_na': np.random.rand(100)
}

# 일부 결측값 생성
data['column_with_na'][::10] = np.nan  # 10개마다 결측값 추가

# 데이터프레임 생성
df = pd.DataFrame(data)

print("결측값 대체 전 데이터프레임:")
print(df.head(15))  # 상위 15개 행 출력

# 결측값이 있는 열과 없는 열 분리
df_with_na = df[df['column_with_na'].isnull()]
df_without_na = df[df['column_with_na'].notnull()]

# 회귀 모델 학습
model = LinearRegression()
model.fit(df_without_na[['feature1', 'feature2']], df_without_na['column_with_na'])

# 결측값 예측
predicted_values = model.predict(df_with_na[['feature1', 'feature2']])

# 예측된 값으로 결측값 대체
df.loc[df['column_with_na'].isnull(), 'column_with_na'] = predicted_values

# 결과 출력
print("결측값 대체 후 데이터프레임:")
print(df.head(15))  # 상위 15개 행 출력
```


### 텍스트 전처리 함수
```
def preprocess_text(text):
    if isinstance(text, float):
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text

df['content'].apply(preprocess_text)
```
### 데이터 스케일링

scaler = StandardScaler() # or MinMaxScaler
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 데이터 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

### 데이터 표준화(학습 및 변환)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

###

data = np.column_stack((X,y))
