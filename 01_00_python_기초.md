
### 하나의 열 선택
single_column = df['content']  # Series 형태

### 여러 열 선택
multiple_columns = df[['content', 'processed_review']]  # DataFrame 형태

### 기본적인 열 처리 함수
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

### map or apply 처리 함수
df['processed_review'] = df['content'].map(preprocess_text)
df['processed_review'] = df['content'].apply(preprocess_text)

df['alive'] = df['alive'].map({'no': 1, 'yes': 0})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2,})

### 특정 열 만 선택
df = df[['content', 'score']]

### Pandas
기본은 행 axis=0 
X = df.drop('data') #는 열이기 떄문에 axis=1 자동 인식
X = df.drop('sdata', axis=1) #가독성을 위해 명시적으로 표시


### lambda x:, (map(), apply(), filter(), sorted())

```
def add_one(x):
    return x + 1 

add_one_lambda = lambda x: x + 1

print(add_one(5))  # 출력: 6 # 일반 함수
print(add_one_lambda(5))  # 출력: 6 # 람다 함수
```


