python_전처리
=============

결측값 처리 : 누락된 값
이상값 처리 : 비상식적으로 큰 값이나 작은 값
중복 데이터 제거 : 동일한 테이터 
데이터 타입 변환 : 데이터 타입 변환
데이터 정규화 : 범위를 일정하게
인코딩 : 범주형을 수치형으로
샘플링 : 데이터 셋의 크기를 줄이거나 늘리기
특징 선택 및 추출 : 중요한 특징 선택 및 새로운 특징 추출

### 1차원 배열 생성
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
```

### 2차원 배열 합치기
```python
data = np.column_stack((A_x, A_y))
```

### 배열을 10x1 형태로 재구성
```python
reshaped_arr = np.array(arr).reshape(-1, 1) # Pandas 2차원화
reshaped_arr = df['컬럼명'].values.reshape(-1, 1) # NumPy 2차원화

```

### 특성과 타겟 분리
```python
X = titanic.drop('survived', axis=1)
y = titanic['survived']
```


### 성별과 탑승한 곳 인코딩
```python
titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic['embarked'] = titanic['embarked'].map({'C': 0, 'Q': 1, 'S': 2})
```

### 결측값 예측 LinearRegression() 
```python
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

### 전체 예제
```python
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
```python
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

# 데이터 스케일링 (학습 및 테스트 분리)
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 데이터 표준화(학습 및 변환)(전체 데이터)
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```