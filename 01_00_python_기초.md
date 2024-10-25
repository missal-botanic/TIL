
### df[df[]]
df[df[]] 형태는 pandas에서 데이터프레임을 필터링하는 방법
filtered_df = df[df['column_name'] > 10]

### range 활용

'id': range(1, 201)

### print 기법
r2 = r2_score(y_te, pre_v) #작동
print(r2 = r2_score(y_te, pre_v)) #미작동
print(r2_score(y_te, pre_v)) #작동

### random number
```
import random
rn = random.random()
```
괄호 안에는 아무것도 들어가지 못함

```
rn = random.random()
df['01'] = [rn for _ in range(100)] # 한번 생성된 값만 저장

df['01'] = [random.random() for _ in range(100)] # 매번 생성

df['01'] = [random.random() for i in range(100)] # 같은 결과
```
```
#03번 기준 전체
df_ori = df[df['03'].isnull()]
df_nan = df[df['03'].notnull()]

#03 번만
df_ori = df[df['03'].isnull()][['03']]
df_nan = df[df['03'].notnull()][['03']]
```

### 선언 뒤 조건 설명 + else
mean_v = df['01'].mean()
df['01'] = df['01'].appy(lambda x: mean_v if x <lower_bound or x > upper_bound else x)


### 하나의 열 선택
single_column = df['content']  # Series 형태

### 여러 열 선택
multiple_columns = df[['content', 'processed_review']]  # DataFrame 형태

### 열의 값이 'positive'인 행들을 필터링합니다.
df['sentiment_label'] == 'positive'
df[df['sentiment_label'] == 'positive'] # 필터링 된 내용을 정의
df[df['sentiment_label'] == 'negative']['content_c'] #그 정의에서 content_c 부분을 선택

데이터프레임 구조
+----+------------------+------------+
|    |   sentiment_label | content_c  |
+----+------------------+------------+
| 0  |        positive   |  'Text A'  |
| 1  |        negative   |  'Text B'  |
| 2  |        positive   |  'Text C'  |
| 3  |        negative   |  'Text D'  |
| 4  |        neutral    |  'Text E'  |
| ...|        ...       |    ...     |
+----+------------------+------------+

행 선택 : df['sentiment_label'] == 'negative'
+----+------------------+------------+
|    |   sentiment_label | content_c  |
+----+------------------+------------+
| 1  |        negative   |  'Text B'  |
| 3  |        negative   |  'Text D'  |
+----+------------------+------------+

열 선택 : 필터링된 데이터에서 ['content_c']를 선택
+------------+
| content_c  |
+------------+
|  'Text B'  |
|  'Text D'  |
+------------+




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

### ' '.join(...):

join 메서드는 문자열을 결합하는 데 사용됩니다.
' '.join(...)는 선택한 긍정적인 리뷰들을 공백을 구분자로 하여 하나의 긴 문자열로 결합합니다.
예를 들어, 긍정적인 리뷰가 ["Great movie!", "Loved it!", "Highly recommend!"]라면, 결과는 "Great movie! Loved it! Highly recommend!"와 같이 됩니다.

###  이미지를 부드럽게
```
plt.imshow(wordcloud, interpolation='bilinear')
```
###  순환돌리기 예시
result = []
for token in word_tokens: 
    if token not in stop_words: 
        result.append(token) 