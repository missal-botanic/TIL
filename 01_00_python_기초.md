
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




print(not a)    # False

x = 10
x = x + 10
x
와
x += 10
같다

비트연산자?



이터레이터



data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 35],
    '직업': ['학생', '회사원', '프리랜서']
}
길이가 같아야 한다

df = pd.DataFrame(data)
df["이름"][0]

inpace= 영구 변환
그냥 set 한번 변환

복합 /= 은 안되도 a=a/n은 될 수 있다.

~반대조건

기본값은 오름 차순 ascending = False 내림차순으로

!pip install matplotlib