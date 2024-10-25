python_데이터 변환
=============

## 데이터 변환

### 특정 열의 데이터 타입을 정수형으로 변환
df['column_name'] = df['column_name'].astype(int)

### 특정 열의 데이터 타입을 문자열로 변환
df['column_name'] = df['column_name'].astype(str)

### 특정 열의 데이터 타입을 부동 소수점으로 변환
df['column_name'] = df['column_name'].astype(float)

----------

## 인코딩(원핫인코딩, 라벨인코딩)
```python
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
df_sampled = df.sample(frac=0.5) # 데이터셋에서 50% 샘플 추출
df_sampled_n = df.sample(n=100) # 데이터셋에서 100개의 샘플 추출
```

frac=0.5를 사용하면 전체 데이터의 비율에 따라 샘플을 추출하고, n=100을 사용하면 원하는 개수만큼 샘플을 선택합니다. 두 방법 모두 데이터 분석이나 모델링에서 데이터의 일부를 랜덤하게 선택할 때 유용하게 사용됩니다.

------------

## 특징 선택 및 추출

### 선택
```python
from sklearn.feature_selection import SelectKBest, f_classif

# 특징 선택 (상위 5개의 특징 선택)
selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X, y)

# 선택된 특징의 인덱스
selected_features = selector.get_support(indices=True)
print(selected_features)
```
### 추출
```python

df['new_feature'] = df['feature1'] * df['feature2'] # 두 열의 곱을 새로운 특징으로 추가
df['new_feature_sum'] = df['feature1'] + df['feature2'] # 두 열의 합을 새로운 특징으로 추가
```