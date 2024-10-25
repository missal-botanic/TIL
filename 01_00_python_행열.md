

### 하나의 열 선택
single_column = df['content']  # Series 형태 특정 컬럼 선택

### 여러 열 선택
multiple_columns = df[['content', 'processed_review']]  # DataFrame 형태

### 특정 열 만 선택
df = df[['content', 'score']]

### 조건에 맞는 행 선택
df[df['Age'] > 30] # 조건에 맞는 행 선택
df["이름"][0] # "이름" 열의 첫 번째 데이터 값을 의미

df_ori = df[df['03'].isnull()]
df_nan = df[df['03'].notnull()] #03번 기준 전체

df_ori = df[df['03'].isnull()][['03']]
df_nan = df[df['03'].notnull()][['03']] #03 번만

------------

### df[df[]] 
filtered_df = df[df['column_name'] > 10] # 데이터프레임을 필터링하는 방법 

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

------------

### 선언 뒤 조건 설명 + else
mean_v = df['01'].mean()
df['01'] = df['01'].appy(lambda x: mean_v if x <lower_bound or x > upper_bound else x)

------------

### 기본적인 열 처리 함수
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1

### map or apply 처리 함수
df['processed_review'] = df['content'].map(preprocess_text)
df['processed_review'] = df['content'].apply(preprocess_text)

df['alive'] = df['alive'].map({'no': 1, 'yes': 0})
df['embarked'] = df['embarked'].map({'C': 0, 'Q': 1, 'S': 2,})

### 기본값은 오름 차순 ascending = False 내림차순으로

### 길이가 같아야 한다

data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 35],
    '직업': ['학생', '회사원', '프리랜서']
}